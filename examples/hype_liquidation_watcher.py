import csv
import os
import time
from datetime import datetime, timezone

from hyperliquid.info import Info
from hyperliquid.utils import constants

COIN = "HYPEUSDC"
LOG_FILE = "hype_events.csv"
TRADE_THRESHOLD = 10000.0
OI_DROP_THRESHOLD = 10000.0
FUNDING_SPIKE_THRESHOLD = 0.001

# "probable liquidation" window in seconds after an OI drop
LIQUIDATION_WINDOW = 2


def to_iso(ts: float) -> str:
    if ts > 1e12:
        ts /= 1000.0
    return datetime.fromtimestamp(ts, tz=timezone.utc).isoformat()


def main() -> None:
    info = Info(constants.MAINNET_API_URL)

    header = [
        "timestamp",
        "event",
        "price",
        "side",
        "size",
        "open_interest",
        "funding_rate",
        "mark_price",
        "notes",
    ]

    # Append to the log so historical data is preserved. If the file is empty
    # write the CSV header before logging events.
    write_header = not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0
    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        if write_header:
            writer.writeheader()

        # Mark the beginning of each run for downstream analysis
        writer.writerow(
            {
                "timestamp": to_iso(time.time()),
                "event": "session_start",
                "price": "",
                "side": "",
                "size": "",
                "open_interest": "",
                "funding_rate": "",
                "mark_price": "",
                "notes": "New logging session started",
            }
        )
        f.flush()

        state = {"open_interest": None, "funding": None, "mark": None}
        # Timestamp of the most recent significant OI drop. Cleared after
        # LIQUIDATION_WINDOW seconds or after one large trade is logged.
        oi_drop_time = None
        next_snapshot_time = time.time() + 300

        def handle_asset(msg):
            nonlocal oi_drop_time, next_snapshot_time
            ctx = msg["data"]["ctx"]
            open_interest = float(ctx["openInterest"])
            funding = float(ctx["funding"])
            mark_px = float(ctx["markPx"])

            notes = []
            event = "asset_update"
            # Detect a large drop in open interest and start the liquidation window
            if state["open_interest"] is not None and open_interest < state["open_interest"] - OI_DROP_THRESHOLD:
                notes.append("open interest drop >10k")
                oi_drop_time = time.time()
                event = "oi_drop"
            if state["funding"] is not None and funding != state["funding"]:
                diff = funding - state["funding"]
                if abs(diff) > FUNDING_SPIKE_THRESHOLD:
                    notes.append("funding spike")
                else:
                    notes.append("funding change")
                event = "funding_update"

            state.update({"open_interest": open_interest, "funding": funding, "mark": mark_px})
            writer.writerow({
                "timestamp": to_iso(time.time()),
                "event": event,
                "price": mark_px,
                "side": "",
                "size": "",
                "open_interest": open_interest,
                "funding_rate": funding,
                "mark_price": mark_px,
                "notes": "; ".join(notes),
            })
            f.flush()

        def handle_trades(msg):
            nonlocal oi_drop_time
            for trade in msg["data"]:
                size = float(trade["sz"])
                if size >= TRADE_THRESHOLD:
                    side = "buy" if trade["side"] == "B" else "sell"
                    notes = ""
                    event = "trade"
                    now = time.time()
                    # If the trade occurs within the liquidation window,
                    # classify it as a liquidation and clear the flag.
                    if oi_drop_time is not None and now - oi_drop_time <= LIQUIDATION_WINDOW:
                        event = "liquidation"
                        notes = "probable liquidation"
                        oi_drop_time = None
                    elif oi_drop_time is not None and now - oi_drop_time > LIQUIDATION_WINDOW:
                        oi_drop_time = None
                    writer.writerow({
                        "timestamp": to_iso(trade["time"]),
                        "event": event,
                        "price": float(trade["px"]),
                        "side": side,
                        "size": size,
                        "open_interest": state["open_interest"],
                        "funding_rate": state["funding"],
                        "mark_price": state["mark"],
                        "notes": notes,
                    })
                    f.flush()

        info.subscribe({"type": "activeAssetCtx", "coin": COIN}, handle_asset)
        info.subscribe({"type": "trades", "coin": COIN}, handle_trades)

        while True:
            time.sleep(1)
            now = time.time()
            # Clear the liquidation flag if the window has elapsed with no trade
            if oi_drop_time is not None and now - oi_drop_time > LIQUIDATION_WINDOW:
                oi_drop_time = None
            if now >= next_snapshot_time:
                writer.writerow({
                    "timestamp": to_iso(now),
                    "event": "snapshot",
                    "price": state["mark"],
                    "side": "",
                    "size": "",
                    "open_interest": state["open_interest"],
                    "funding_rate": state["funding"],
                    "mark_price": state["mark"],
                    "notes": "",
                })
                f.flush()
                next_snapshot_time += 300


if __name__ == "__main__":
    main()
