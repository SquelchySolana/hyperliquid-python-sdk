"""Real-time spoofing and trap detection for HYPE perp.

This script monitors the L2 order book and trades on Hyperliquid using the
public Info websocket. Large (>10k HYPE) orders are tracked and potential spoof
behaviour is flagged:

- ``quick_cancel``  : order disappeared within 60s without trading
- ``low_trade``     : removed after <10% of size was traded
- ``real_defense``  : order actually filled (>=10% traded)
- ``rug_pull_cluster`` : multiple large walls pulled together as price
  approaches

Events are written to ``flagged_events.csv`` and printed to the console.  The
Hyperliquid matching engine processes cancels before new orders each block,
which means large walls disappearing just as price nears them are actionable
signals for potential spoofing or trap behaviour.
"""

from __future__ import annotations

import csv
import time
from collections import deque
from typing import Deque, Dict, Tuple

from hyperliquid.info import Info
from hyperliquid.utils import constants

THRESHOLD = 10_000  # minimum order size considered significant
COIN = "HYPE"
CSV_FILE = "flagged_events.csv"

# order_book keeps the latest snapshot of each side
order_book: Dict[str, Dict[float, float]] = {"A": {}, "B": {}}

# tracked_orders stores details about currently observed large orders
# key -> (side, price)
# value -> {"size": float, "start": float, "traded": float}
tracked_orders: Dict[Tuple[str, float], Dict[str, float]] = {}

# Recent cancel timestamps for rug-pull cluster detection
recent_cancels: Deque[Tuple[float, str, float, float]] = deque()
CLUSTER_WINDOW = 10.0  # seconds within which multiple cancels trigger a cluster flag


def log_flagged(event_type: str, side: str, price: float, size: float, notes: str) -> None:
    """Append a flagged event to the CSV and print it."""
    timestamp = int(time.time() * 1000)
    with open(CSV_FILE, "a", newline="") as f:
        csv.writer(f).writerow([timestamp, event_type, price, side, size, notes])
    print(f"FLAGGED: {timestamp}, {event_type}, {price}, {side}, {size}, {notes}")


def handle_cluster(side: str, price: float, size: float) -> None:
    """Check if several large orders were canceled together."""
    now = time.time()
    recent_cancels.append((now, side, price, size))
    while recent_cancels and now - recent_cancels[0][0] > CLUSTER_WINDOW:
        recent_cancels.popleft()
    if len(recent_cancels) >= 2:
        log_flagged("rug_pull_cluster", side, price, size, "multiple large walls removed together")
        recent_cancels.clear()


def check_spoofing(side: str, price: float) -> None:
    """Evaluate a tracked order when it disappears or drops below threshold."""
    info = tracked_orders.pop((side, price), None)
    if info is None:
        return

    lifetime = time.time() - info["start"]
    traded = info["traded"]
    size = info["size"]

    if traded >= size * 0.1:
        event = "real_defense"
        note = "order traded >=10% before removal"
    elif lifetime < 60 and traded == 0:
        event = "quick_cancel"
        note = "order canceled <60s with no trades"
    else:
        event = "low_trade"
        note = f"only {traded:.2f} traded before remove"

    log_flagged(event, side, price, size, note)
    handle_cluster(side, price, size)


def handle_side(side: str, levels) -> None:
    """Process order book levels for a side."""
    prev = order_book[side]
    new: Dict[float, float] = {}

    for level in levels:
        price = float(level["px"])
        size = float(level["sz"])
        new[price] = size

        if price not in prev:
            if size >= THRESHOLD:
                tracked_orders[(side, price)] = {"size": size, "start": time.time(), "traded": 0.0}
        else:
            prev_size = prev[price]
            if size < THRESHOLD <= prev_size:
                check_spoofing(side, price)
            elif size >= THRESHOLD:
                tracked_orders[(side, price)]["size"] = size

    for price, prev_size in prev.items():
        if price not in new and prev_size >= THRESHOLD:
            check_spoofing(side, price)

    order_book[side] = new


def on_book(msg) -> None:
    data = msg["data"]
    bids, asks = data["levels"]
    handle_side("B", bids)
    handle_side("A", asks)


def on_trades(msg) -> None:
    for trade in msg["data"]:
        px = float(trade["px"])
        sz = float(trade["sz"])
        for (side, price), info in tracked_orders.items():
            if side == "B" and px <= price:
                info["traded"] += sz
            elif side == "A" and px >= price:
                info["traded"] += sz


def main() -> None:
    info = Info(constants.MAINNET_API_URL)
    info.subscribe({"type": "l2Book", "coin": COIN}, on_book)
    info.subscribe({"type": "trades", "coin": COIN}, on_trades)
    print("Monitoring started. Press Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        info.disconnect_websocket()


if __name__ == "__main__":
    main()
