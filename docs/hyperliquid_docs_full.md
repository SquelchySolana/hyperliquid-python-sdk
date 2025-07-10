
# Hyperliquid Docs

---

## Table of Contents

- [1. About Hyperliquid](#1-about-hyperliquid)
- [2. Onboarding](#2-onboarding)
- [3. HyperCore](#3-hypercore)
- [4. HyperEVM](#4-hyperevm)
- [5. Hyperliquid Improvement Proposals (HIPs)](#5-hyperliquid-improvement-proposals-hips)
- [6. Trading](#6-trading)
- [7. Margin Calculation Examples](#7-margin-calculation-examples)
- [8. API & Developer Resources](#8-api--developer-resources)
- [9. Audit Reports & Security](#9-audit-reports--security)
- [10. FAQ](#10-faq)
- [11. Glossary](#11-glossary)
- [12. References](#12-references)

---

# 1. About Hyperliquid

### 1.1 What is Hyperliquid?

Hyperliquid is a performant blockchain built with the vision of a fully onchain open financial system.
Liquidity, user applications, and trading activity synergize on a unified platform that will ultimately house all of finance.

---

### 1.2 Technical Overview

* Hyperliquid is a layer one blockchain (L1) written and optimized from first principles.
* Uses a custom consensus algorithm called **HyperBFT** inspired by Hotstuff and its successors.
* Both the algorithm and networking stack are optimized from the ground up to support the unique demands of the L1.

#### State Execution:

* Split into two broad components:
  * **HyperCore:**
    * Fully onchain perpetual futures and spot order books.
    * Every order, cancel, trade, and liquidation happens transparently with one-block finality.
    * Supports 200k orders/sec, with throughput improving as node software is optimized.
  * **HyperEVM:**
    * Brings Ethereum-style smart contract platform to Hyperliquid blockchain.
    * Offers performant liquidity and financial primitives of HyperCore as permissionless building blocks.
    * See the HyperEVM documentation for more technical details.

---

### 1.3 Core Contributors

* **Hyperliquid Labs** is the core contributor, led by Jeff and iliensinc (Harvard classmates).
* Team includes members from Caltech, MIT, Airtable, Citadel, Hudson River Trading, Nuro.
* Originally did proprietary crypto market making, then expanded into DeFi in summer 2022.
* Frustrated by issues in existing platforms (bad market design, tech, UX), so they built a better system.
* Actively engages with and listens to the community (Discord server available for questions/feedback).
* Hyperliquid Labs is self-funded and has not taken any external capital—focuses on independent product vision.

---

# 2. Onboarding

### 2.1 How to Start Trading

**What do I need to trade on Hyperliquid?**

* You can trade with a normal DeFi wallet or log in with your email address.

#### **If using a normal DeFi wallet:**

1. **An EVM wallet**

   * (e.g., Rabby, MetaMask, WalletConnect, Coinbase Wallet)
   * Set one up at [rabby.io](https://rabby.io/)
   * After downloading wallet extension, create a new wallet.
   * **IMPORTANT:** Your wallet has a secret recovery phrase—anyone with access can control your funds. Never share your private key or seed phrase. Write it down and store safely.

2. **Collateral**

   * USDC and ETH (gas to deposit) on Arbitrum, or
   * BTC on Bitcoin, ETH on Ethereum, SOL or FARTCOIN on Solana (which can be traded for USDC on Hyperliquid order books)

---

**How do I onboard to Hyperliquid?**

* **If logging in with email:**

  1. Click "Connect" and enter your email address.
  2. Enter the 6-digit code sent to your email.
  3. Once connected, deposit funds—your blockchain address is created for your email.
  4. Send USDC (Arbitrum), BTC (Bitcoin), ETH (Ethereum), or SOL/FARTCOIN (Solana) as collateral.

* **If onboarding with a DeFi wallet:**

  1. Once you have EVM wallet & collateral, go to [app.hyperliquid.xyz/trade](https://app.hyperliquid.xyz/trade)
  2. Click “Connect” and choose wallet to connect.
  3. Sign gas-less transaction when prompted.
  4. Deposit funds (choose between USDC on Arbitrum, BTC on Bitcoin, ETH on Ethereum, SOL/FARTCOIN on Solana).
  5. For USDC: Enter deposit amount, click “Deposit”, confirm in wallet.
  6. For BTC, ETH, SOL, FARTCOIN: Send asset to destination address shown.
     *Note: Only USDC is used as trading collateral; you must sell other assets for USDC to trade perps or spot assets.*

* **You’re now ready to trade!**

---

**How do I trade perpetuals on Hyperliquid?**

* Use USDC as collateral to long/short tokens (no need to own the token).
* Select token with the token selector.
* Decide to long (price up) or short (price down).
* Set position size (leverage * collateral).
* Click “Place Order” and then confirm.
* (Optional: Check "Don’t show this again" to skip confirmation modal.)

---

**How do I bridge USDC onto Hyperliquid?**

* Need ETH & USDC on Arbitrum (Hyperliquid native bridge is between HL and Arbitrum; ETH is for deposit gas).
* No gas for trading on Hyperliquid.

**You can use:**

* [Arbitrum Bridge](https://bridge.arbitrum.io/)
* [deBridge](https://app.debridge.finance/)
* [Mayan Finance](https://swap.mayan.finance/)
* [Across](https://app.across.to/bridge?)
* [Router Nitro](https://routernitro.com/swap)
* [Jumper Exchange](https://jumper.exchange/)
* [Synapse Protocol](https://synapseprotocol.com/)
* Or, move funds directly from a CEX to Arbitrum.
* Once ETH & USDC are on Arbitrum, deposit via “Deposit” button at [app.hyperliquid.xyz/trade](https://app.hyperliquid.xyz/trade).

---

**How do I withdraw USDC from Hyperliquid?**

* Go to [app.hyperliquid.xyz/trade](https://app.hyperliquid.xyz/trade), click “Withdraw” (bottom right).
* Enter USDC amount, click “Withdraw to Arbitrum.”
* No gas fee for withdrawal—there’s a $1 withdrawal fee.

---
### 2.2 How to Use the HyperEVM

---

#### For Users:

**How do I add the HyperEVM to my wallet extension?**

* You can add the HyperEVM to your wallet using [Chainlist](https://chainlist.org/chain/999) or manually:

  * In your wallet extension, click **“Add Custom Network”** and enter:

    * Chain ID: `999`
    * Network Name: `Hyperliquid`
    * RPC URL: `https://rpc.hyperliquid.xyz/evm`
    * Block explorer URL (optional):

      * [https://purrsec.com/](https://purrsec.com/)
      * [https://hyperliquid.cloud.blockscout.com/](https://hyperliquid.cloud.blockscout.com/)
      * *(Other explorers coming soon, thanks to community members!)*
    * Currency Symbol: `HYPE`

---

**How do I move assets to and from the HyperEVM?**

* Click “Transfer to/from EVM” on the Balances table of the Trade or Portfolio pages, or “EVM <-> Core Transfer” at the top of the Portfolio page.
* You can send HYPE to `0x2222222222222222222222222222222222222222` from either your Spot balances or from the EVM to transfer.

  * **Note:** This only works for HYPE; sending other assets to this address will result in loss. Each spot asset has a unique transfer address.
* Sending from HyperEVM to Spot costs gas in HYPE (on HyperEVM).
* Sending from Spot to HyperEVM costs gas in HYPE (on HyperCore/Spot).

---

**What can I do on the HyperEVM?**

* Various teams are building applications, tooling, etc. on the HyperEVM.
* Track new releases and projects:

  * [hypurr.co/ecosystem-projects](https://www.hypurr.co/ecosystem-projects)
  * [hyperliquid.wiki](https://hyperliquid.wiki/)
  * [data.asxn.xyz dashboard](https://data.asxn.xyz/dashboard/hyperliquid-ecosystem)
  * `#hyperevm-eco` channel in the [Hyperliquid Discord](https://discord.gg/hyperliquid)

---

**How does the HyperEVM interact with the rest of the Hyperliquid blockchain?**

* Hyperliquid consists of **HyperCore state** (perps, spot, order books, trading features) and **HyperEVM state**.
* Both are secured by the same HyperBFT consensus—ultimate goal is seamless integration.
* Apps built on HyperEVM (lending, trading, yield, etc.) can directly access orderbook liquidity, giving DeFi CEX-like functionality.
* Application tokens can list natively on Hyperliquid permissionlessly—trading and building on the same chain.

---

**Why does gas spike?**

* Hyperliquid blockchain is highly performant, but HyperEVM was intentionally launched with lower initial throughput for safety.
* Since HyperCore and HyperEVM share state, initial HyperEVM bandwidth is restricted, but will be increased over time.
* Gas spikes when demand > supply for blockspace, same as on Ethereum/L2s.
* HyperEVM uses EIP-1559 fee structure (base + priority fee):
  [EIP-1559 reference](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1559.md)

---

**Can I send HYPE on the HyperEVM to a centralized exchange?**

* Always confirm with the CEX if they support HyperEVM!
* HyperEVM is part of the Hyperliquid blockchain, but separate from HyperCore (perps, spot, etc.).
* Some CEXs only support HYPE from Spot balances on HyperCore—not HyperEVM.
* **Do a test transaction first** if unsure.

---

**How do I bridge assets to the HyperEVM from another chain?**

* Use one of many bridges/swaps:

  * LayerZero: [hyperbridge.xyz](https://www.hyperbridge.xyz/)
  * DeBridge: [app.debridge.finance](https://app.debridge.finance/)
  * Gas.zip: [gas.zip](https://www.gas.zip/)
  * Jumper: [jumper.exchange](https://jumper.exchange/)
  * Cortex for HYPE: [cortexprotocol.com](https://cortexprotocol.com/agent?q=buy%20hype)
  * Garden for BTC: [app.garden.finance](https://app.garden.finance/)
  * Mintify for ETH: [mintify.xyz/crypto](https://mintify.xyz/crypto)
  * USDT0 for USDT0: [usdt0.to/transfer](https://usdt0.to/transfer)
  * Stargate for USDe: [stargate.finance/bridge](https://stargate.finance/bridge?srcChain=ethereum&srcToken=0x4c9EDD5852cd905f086C759E8383e09bff1E68B3&dstChain=hyperliquid&dstToken=0x5d3a1Ff2b6BAb83b63cd9AD0787074081a52ef34)

---

#### For Builders:

**What can I build on the HyperEVM?**

* Any EVM-compatible application (just like on other chains).
* HyperEVM is fully functional; features from testnet will gradually roll to mainnet.

**How do I set up an RPC? What RPCs are available?**

* Hosted RPC: `https://rpc.hyperliquid.xyz/evm`
* Community members are launching more RPCs.
* Running your own node is optional—all data is uploaded in real-time to S3.
* See Python SDK example:
  [evm_block_indexer.py](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/master/examples/evm_block_indexer.py)

**How do I get gas on the HyperEVM?**

* Native token is HYPE.
* Buy HYPE with USDC on Hyperliquid, then transfer from HyperCore to HyperEVM.
* Or use one of the above bridges.

**What version of the EVM is the HyperEVM based on?**

* Cancun without blobs.

**What is the difference between the HyperEVM and other EVMs, like Ethereum?**

* Functionality is largely the same; tooling and applications are portable.
* Main differences:

  * Dual block system: fast small blocks and slow big blocks.
  * Seamless interactions with the native Hyperliquid state (lets DeFi use CEX-like liquidity).

---

### 2.3 How to Stake HYPE

You can use different websites to stake HYPE on HyperCore, including:

* [app.hyperliquid.xyz/staking](https://app.hyperliquid.xyz/staking/)
* [stake.nansen.ai/stake/hyperliquid](https://stake.nansen.ai/stake/hyperliquid)
* [app.validao.xyz/stake/hyperliquid](https://app.validao.xyz/stake/hyperliquid)
* [hypurrscan.io/staking](https://hypurrscan.io/staking)

**Steps:**

* You need HYPE in your **Spot Balance on HyperCore**.
  If your HYPE is on the HyperEVM, transfer it to HyperCore.
* Transfer HYPE from your Spot Balance to your Staking Balance.
* Choose a validator to stake to.

  * **Staking lockup:** 1 day.
* To unstake:

  1. Unstake from a validator.
  2. Transfer from your Staking Balance to your Spot Balance (this takes 7 days).
  3. After 7 days, HYPE will appear in your Spot Balance.

For further questions, refer to the Staking section.

---

### 2.4 Testnet Faucet

* To use the testnet faucet, you must have deposited on mainnet with the **same address**.
* You can then claim **1,000 mock USDC** from the testnet faucet:
  [app.hyperliquid-testnet.xyz/drip](https://app.hyperliquid-testnet.xyz/drip)

---

-------------------------------------------------------------------------------------------------------------------------------------

## 3. HyperCore

---

### 3.1 Overview

**Consensus:**

* Hyperliquid is secured by **HyperBFT**, a variant of HotStuff consensus.
* Like most proof of stake chains, blocks are produced by validators in proportion to native token staked.

**Execution:**

* Hyperliquid state = HyperCore + HyperEVM.
* **HyperCore** includes margin and matching engine state.

  * Does NOT rely on off-chain order books.
  * Core design = full decentralization, consistent transaction ordering via HyperBFT consensus.

**Latency:**

* Uses optimized HyperBFT for low end-to-end latency.
* Median 0.2s and 99th percentile 0.9s (from colocated client to committed response).
* Fast enough for automated trading strategies and responsive UI.

**Throughput:**

* Mainnet supports ~200k orders/sec.
* Bottleneck is currently execution; consensus/network stack can scale to millions/sec once execution is optimized further.

---

### 3.2 Bridge

* **Deposits** to the bridge:

  * Signed by validators; credited when >2/3 staking power has signed.
* **Withdrawals**:

  * Immediately deducted from L1 balance, validators sign as separate transactions.
  * When 2/3 staking power has signed, an EVM tx can be sent to the bridge to request withdrawal.
  * After withdrawal is requested, there’s a dispute period—bridge can be locked for malicious withdrawals.
  * **Unlocking** requires cold wallet signatures from 2/3 stake-weighted validators.
  * After dispute, finalization transactions distribute USDC to destination addresses.
* **Validator management:**

  * Mechanism to maintain active validator set and stakes on the bridge contract.
* **User experience:**

  * No Arbitrum ETH needed for withdrawal. Instead, a $1 USDC withdrawal gas fee is paid on Hyperliquid.
  * Bridge/audit logic is public—audited by Zellic (see GitHub/Audits section).

---

### 3.3 API Servers

* **API servers** listen to node updates and maintain blockchain state locally.
* Serve info about blockchain state and forward user transactions to node.
* **Data sources:** REST and WebSocket.
* **Workflow:**

  * User tx sent to API server → forwarded to node → gossiped via HyperBFT consensus.
  * When tx is included in committed block, API server responds to original request with L1 execution response.

---

### 3.4 Clearinghouse

* **Perps clearinghouse** (on HyperCore):

  * Manages perps margin state for each address (balances and positions).
  * Deposits are credited to cross margin balance by default.
  * Positions opened in **cross margin** by default; **isolated margin** also supported (allocates margin to specific position, separates liquidation risk).
* **Spot clearinghouse**:

  * Manages spot user state (token balances and holds) for each address.

---

### 3.5 Oracle

* Validators publish **spot oracle prices** for each perp asset every 3 seconds.
* Oracle prices are used for:

  * Computing funding rates
  * Mark price (used for margin, liquidations, and triggering TP/SL orders)
* **Computation:**

  * Each validator computes spot oracle price as weighted median of Binance, OKX, Bybit, Kraken, Kucoin, Gate IO, MEXC, and Hyperliquid spot prices.
  * Weights: 3, 2, 2, 1, 1, 1, 1, 1.
  * For perps with primary spot liquidity on Hyperliquid (e.g., HYPE): No external sources in oracle until liquidity is sufficient.
  * For perps with primary liquidity outside Hyperliquid (e.g., BTC): Hyperliquid spot price not included in oracle.
* **Final oracle price** is weighted median of all validator oracle prices (validators weighted by stake).

---

### 3.6 Order Book

* **HyperCore state** includes an order book for each asset (works like centralized exchanges).
* **Order properties:**

  * Price = integer multiple of tick size.
  * Size = integer multiple of lot size.
  * Orders matched in price-time priority.
* **Margin checks:**

  * Perp asset order book ops reference the clearinghouse (margin/position checks on both open and resting side).
  * Ensures margin system is consistent even if oracle price fluctuates after order is placed.
* **Consensus/mempool:**

  * Hyperliquid L1 mempool and consensus logic are **semantically aware** of transactions that interact with HyperCore order books.
  * **Within a block:**

    1. Actions that don’t send GTC/IOC orders to any book
    2. Cancels
    3. Actions that send at least one GTC/IOC

    * Within each category, sorted by order proposed by block proposer.
    * Modifies categorized by new order they place.

---
### 3.7 Staking

**Basics**

* HYPE staking happens within HyperCore.
* Like USDC, HYPE can be transferred between spot and staking accounts.
* Within staking account, HYPE can be staked (“delegated”) to any number of validators (delegated proof of stake).
* **Validator Requirements:**

  * Must self-delegate 10,000 HYPE to become active.
  * Active validators produce blocks and receive rewards proportional to delegated stake.
  * Validators may charge commission to delegators.

    * Commission cannot be increased unless new commission ≤ 1% (prevents bait-and-switch).
* **Delegation/Unstaking:**

  * Delegations have a **1-day lockup**. After that, you can partially or fully undelegate any time.
  * Undelegated HYPE instantly appears in your staking account balance.
  * Transfers from **spot → staking** are instant.
  * Transfers from **staking → spot** have a **7-day unstaking queue** (prevents rapid large-scale attacks, standard in PoS).

    * Example: Stake→spot transfer of 100 HYPE at 08:00 UTC Mar 11 = finalizes 08:00 UTC Mar 18.
* **Rewards:**

  * Formula inspired by Ethereum: reward rate is **inversely proportional to √(total HYPE staked)**.
  * At 400M total HYPE staked, yearly reward ≈ 2.37%.
  * Rewards come from the emissions reserve, accrue every minute, distributed daily, and are **compounded** to the staked validator.
* **Technical Details:**

  * “Quorum” = any set of validators >2/3 total stake (needed for consensus).
  * Stakers must only delegate to trusted validators (security).
  * **Consensus rounds**: each is a batch of txs plus quorum validator signatures, resulting in a new execution state block (height increments only on tx rounds).
  * **Validator set** evolves in epochs of 100,000 rounds (~90min).
  * Validators can **jail** peers for poor performance (not slashing); jailed = no rewards.
  * Jailing ≠ slashing. Slashing is only for provable malicious behavior.

---

### 3.12 Multi-sig

**Advanced Feature**

* HyperCore supports **native multi-sig** actions (multiple keys control a single account).
* Unlike many chains, multi-sig is a built-in primitive, not just a smart contract.

**Workflow:**

* Convert a user to multi-sig by sending a `ConvertToMultiSigUser` action with authorized users and minimum signers required.
* Authorized users must be existing Hyperliquid users.
* After conversion, all actions must be sent via multi-sig.
* Each authorized user signs a payload; MultiSig action wraps any normal action and includes signatures.
* Payload includes the target multi-sig user and the authorized user (leader) who sends the final action.
* Only the nonce of the sending authorized user is validated/updated.
* The leader can also be an API wallet.
* To update the set of authorized users/threshold, send a MultiSig action wrapping a new `ConvertToMultiSigUser` with updated state.
* To revert to a normal user, send `ConvertToMultiSigUser` with an empty set via multi-sig.

**Misc Notes:**

* Leader (tx lead) must be an authorized user, not the multi-sig account.
* All signatures must use same nonce, tx lead, etc.
* Leader collects all signatures before submitting.
* Users can be multi-sig users and authorized users for other multi-sig users at the same time.
* Max 10 authorized users per multi-sig user.

**HyperEVM warning:**
Converting to multi-sig does NOT prevent HyperEVM user control by the original wallet. Multi-sig users should generally not interact with HyperEVM before/after conversion.

**See the Python SDK for code examples.**

---

## 4. HyperEVM

---

### 4.1 HyperEVM Overview

* The Hyperliquid blockchain features two key parts: **HyperCore** and **HyperEVM**.
* **HyperEVM is *not* a separate chain**—it’s secured by the same HyperBFT consensus as HyperCore.
* This allows HyperEVM to interact directly with HyperCore features, such as spot and perp order books.

**What can I do on the HyperEVM?**

* Explore directories of apps, tools, and community projects:

  * HypurrCo
  * ASXN
  * Hyperliquid.wiki
* Visit the HyperEVM onboarding FAQ for more details.

**Why build on the HyperEVM?**

* Builders can access mature, liquid, performant onchain order books (via HyperCore + HyperEVM).
* Hyperliquid has a vibrant user base eager to try new applications and onchain finance.
* See the HyperEVM developer section for more technical details and tools.

**Examples:**

* *ERC20 & Spot Asset Listing:*

  * Deploy ERC20 contract on HyperEVM with standard tooling.
  * Deploy a corresponding spot asset permissionlessly in HyperCore spot auction.
  * Link HyperCore token and HyperEVM contract: use same token in EVM apps and native spot trading—**no permission or bridging risk**.
* *Lending Protocols:*

  * Set up pool contract that accepts token XYZ as collateral, lends token ABC.
  * Lending contract can read XYZ/ABC prices directly from HyperCore order books (via precompile).
  * If liquidation required, smart contract can send swap orders directly on HyperCore order books (via write system contract).
  * In Solidity, these are simple built-in functions.
  * Enables protocolized liquidations similar to perps on HyperCore—**deep liquidity abstracted for arbitrary apps**.

**What stage is the HyperEVM in?**

* **Alpha stage:**

  * Gradual rollout—no “insiders,” equal access, level playing field.
  * Did not launch with all tooling found on other chains (fair/neutral launch).
  * Safer upgrade path for complex, high-volume system; avoids downtime.
  * MVP shipped and iterated live with user feedback; hardened by real economic use.
  * **Higher throughput and write system contracts** coming soon.

---

### 4.2 Tools for HyperEVM Builders

**EVM RPCs**

* Mainnet: `https://rpc.hyperliquid.xyz/evm`
* Testnet: `https://rpc.hyperliquid-testnet.xyz/evm`
* HypurrScan: `http://rpc.hypurrscan.io`
* Stakely: `https://hyperliquid-json-rpc.stakely.io`
* Quicknode: `https://www.quicknode.com/chains/hyperliquid`
* Chainstack: `https://chainstack.com/build-better-with-hyperliquid/`

**EVM RPCs with archive node support**

* HypeRPC by Imperator: `https://hyperpc.app/`
* Proof Group: `https://www.purroofgroup.com/`
* Altitude: `https://rpc.reachaltitude.xyz/`

**Native gas**

* Gas.zip: [https://www.gas.zip/](https://www.gas.zip/)
* DeBridge: [https://app.debridge.finance/](https://app.debridge.finance/)
* Cortex: [https://cortexprotocol.com/agent?q=buy%20hype](https://cortexprotocol.com/agent?q=buy%20hype)

**Big block/small block toggle**

* [Block toggle app](https://hyperevm-block-toggle.vercel.app)

**Python SDK example**

* [basic_evm_use_big_blocks.py](https://github.com/hyperliquid-dex/hyperliquid-python-sdk/blob/master/examples/basic_evm_use_big_blocks.py)

**Oracles**

* Pyth: [Pyth price feeds](https://docs.pyth.network/price-feeds/contract-addresses/evm)
* Stork: [Stork price feeds](https://docs.stork.network/resources/contract-addresses/evm#hyperevm)
* Redstone: [Redstone feeds](https://app.redstone.finance/app/feeds/?page=1&sortBy=popularity&sortDesc=false&perPage=32&networks=999,998)
* Blocksense: [Blocksense price feeds](https://coda.io/@georgi-zlatarev/blocksense-hyperevm-price-feeds)

**Crosschain messaging**

* LayerZero: [LayerZero deployments](https://docs.layerzero.network/v2/deployments/deployed-contracts?chains=hyperliquid)
* DeBridge: [DeBridge deployed contracts](https://docs.debridge.finance/the-debridge-messaging-protocol/deployed-contracts#evm-chains)
* Hyperlane: [Hyperlane reference](https://docs.hyperlane.xyz/docs/reference/default-ism-validators)

**Indexing / subgraphs**

* Goldsky: [Goldsky docs](https://docs.goldsky.com/chains/hyperevm)
* Allium: [Allium docs](https://docs.allium.so/historical-chains/supported-blockchains/hyperliquid)
* SQD: [SQD docs](https://docs.sqd.ai/hyperliquid-support/)

**SAFE multi-sig instances**

* Den: [safe.onchainden.com](https://safe.onchainden.com/welcome)
* Palmera: [Palmera DAO](https://x.com/palmera_dao/status/1899460307401019488)

**MPC multi-sig**

* Fireblocks: [fireblocks.com](https://www.fireblocks.com/integrations/protocols/)
* Tholos: [tholos.app](https://www.tholos.app/)

**Smart contract tooling**

* Gelato: [Gelato docs](https://docs.gelato.network/web3-services)
* Proof of Play RNG: [Proof of Play](https://docs.proofofplay.com/services/vrng/about)

**Account abstraction**

* ZeroDev: [ZeroDev docs](https://docs.zerodev.app/)

---

## 5. Hyperliquid Improvement Proposals (HIPs)

---

### 5.1 HIP-1: Native Token Standard

* **HIP-1** is a capped supply fungible token standard.
* Features onchain spot order books between pairs of HIP-1 tokens.

**Token Genesis Parameters:**

* **name:** Human readable, max 6 characters (no uniqueness constraint).
* **weiDecimals:** Conversion rate from minimal integer unit to human-readable float (e.g., ETH = 18, BTC = 8).
* **szDecimals:** Minimum tradable decimals (lot size on order books is `10 ** (weiDecimals - szDecimals)`).

  * Must satisfy: `szDecimals + 5 <= weiDecimals`.
* **maxSupply:** Maximum and initial supply (can decrease over time due to fees or burns).
* **initialWei:** (Optional) Genesis balances specified by deployer (e.g., treasury, bridge mint, etc.).
* **anchorTokenWei:** Optionally specify existing HIP-1 tokens to proportionally receive genesis balances.
* **hyperliquidityInit:** Parameters to initialize Hyperliquidity for USDC spot pair (see HIP-2 for details).

**Deployment:**

* Deployment tx generates a unique hash for the token.
* **Gas cost:**

  * Paid in HYPE, decided by Dutch auction (31-hour duration).
  * Gas starts at `initial_price`, decreases linearly to 500 HYPE.
  * Initial price is 500 HYPE if last auction failed; otherwise, 2x last gas price.
* Genesis to existing anchor tokens holders is proportional to balance (must be at least 0.0001% of anchor’s max supply).
* A small initial USDC gas fee (TBD) may be required for the first state update of each (address, token) pair; future trades and transfers are gas free (within normal fill rate).

**Important Gas Details:**

* **Time-sensitive step:** Deploying the token (specifying name, szDecimals, weiDecimals).

  * Gas is charged and token is locked at this step.
  * No time limit after gas is paid.
* **Complex/multi-stage:** Deployment can get stuck (e.g., Hyperliquidity and total supply mismatch).

  * **Try on testnet first:** [Hyperliquid Testnet Spot Deployment](https://app.hyperliquid-testnet.xyz/deploySpot)
  * **No gas refund if stuck.**

---

**USDC**

* USDC is used for all perps margining.
* With HIP-1, USDC becomes a spot token with atomic transfers between perps and spot wallets.
* **Spot USDC:** `szDecimals = weiDecimals = 8` (for a wide range of token prices).

---

**Spot Trading**

* HIP-1 tokens trade on order books parameterized by base and quote tokens.
* Limit orders exchange

  * `sz * 10 ** (weiDecimalsBase - szDecimalsBase)` units of base
  * for `px * sz * 10 ** (weiDecimalsQuote - szDecimalsQuote)` units of quote.
* Every HIP-1 token gets a native spot order book with Spot USDC as quote.
* Trading of arbitrary pairs of native tokens may be enabled in the future.

---

### 5.2 HIP-2: Hyperliquidity

**Motivation:**

* HIP-1 is sufficient as a permissionless token standard, but new tokens often require bootstrapped liquidity.
* Hyperliquid’s design principle: **liquidity should be democratized**.

  * For perps, HLP provides deep liquidity based on CEX prices.
  * For early HIP-1 tokens, a new model is needed.

**Hyperliquidity:**

* Inspired by Uniswap, but interoperates with Hyperliquid’s native onchain order book.
* HIP-2 is a **fully decentralized, onchain strategy**—part of Hyperliquid's block transition logic.
* **No operators:**

  * The strategy is run by consensus, just like the order book (no off-chain bots or actors).

**Parameters:**

* **spot:** The spot asset (must be a USDC-quoted HIP-1 token).
* **startPx:** Initial price of the liquidity range.
* **nOrders:** Number of orders in the range.
* **orderSz:** Size of each order in the range.
* **nSeededLevels:** Number of levels starting as bids (not asks).

  * For each additional seeded level, deployer must fund `price × size` worth of USDC.
  * More seeded bids = lower initial Hyperliquidity supply, as it reduces genesis supply.

**Price Range Construction:**

* Price levels are recursively defined:

  * `px_0 = startPx`
  * `px_i = round(px_{i-1} * 1.003)` (each price is 0.3% above the last)
* **Strategy updates** on every block where at least 3 seconds have elapsed since the previous update block.

**After Each Update:**

1. **Order Management:**

   * Targets `nFull = floor(balance / orderSz)` full ask orders.
   * Plus a possible partial ask order if remainder exists.
   * Ensures these orders (as ALO) are posted unless rejected.
2. **Order Reallocation:**

   * Each fully filled tranche is re-allocated as an order of `orderSz` on the side with available balance, except the single partial order if it exists.

**Key Properties:**

* Guarantees a **0.3% spread** every 3 seconds.
* **No user maintenance required** (no need for user txs to keep liquidity live).
* Unlike Uniswap/AMMs, Hyperliquidity is a participant in a general-purpose order book—**active users can always add their own liquidity** alongside.

------------------------------------------------------------------


### 5.3 HIP-3: Builder-Deployed Perpetuals

**Advanced Feature – Testnet Only**

* The Hyperliquid protocol will support **builder-deployed perps (HIP-3)**—a major step toward fully decentralized perpetual market listings.
* **MVP is live on testnet.** Feedback is encouraged (numbers/specs below may change).

**Key Features:**

* Deployments create new, performant onchain order books on HyperCore.
* **Deployment gas** is paid in HYPE, via Dutch auction every 31 hours.
* Deployers can set a **fee share up to 50%** (configurable on top of the base fee rate; applies to total fee).
* **Deployments are permissionless.**

**Deployer Responsibilities:**

* **Market definition:** Set oracle definition and contract specs.
* **Market operation:**

  * Set oracle prices.
  * Set leverage limits.
  * Settle the market if needed.
* **Composability:**

  * Perp deployment supports HyperCore multi-sig for protocolized market deployment and operation.

**Quality & Safety:**

* Deployers must maintain **1 million staked HYPE**.
* For user protection, in the event of malicious market operation, **validators can slash the deployer’s stake** (stake-weighted vote during deployer’s 7-day unstaking queue).

------------------------------------------------------------------------

### 5.4 Frontend Checks

There are many ways to reach invalid configurations during the spot deploy process. To avoid this, deployers can try intended deployments on testnet first. For automated deployment integrations, the following is a list of client-side checks that may be helpful.

**Token Deployment**

```js
if (szDecimals === undefined || weiDecimals === undefined) {
  displayAlert(
    "Size decimals and Wei decimals must be specified.",
    "error"
  );
  return;
}
if (szDecimals > 2 || szDecimals < 0) {
  displayAlert("Size decimals must be between 0 and 2.", "error");
  return;
}
if (weiDecimals > 8 || weiDecimals < 0) {
  displayAlert("Wei decimals must be between 0 and 8.", "error");
  return;
}
if (szDecimals + 5 > weiDecimals) {
  displayAlert("weiDecimals must be at least szDecimals + 5.", "error");
  return;
}
```

**Set Deployer Trading Fee Share**

```js
if (deployerTradingFeeShare === undefined) {
  displayAlert("Deployer trading fee share must be specified.", "error");
  return;
}

if (deployerTradingFeeShare < 0 || deployerTradingFeeShare > 100) {
  displayAlert(
    "Deployer trading fee share must be between 0 and 100.",
    "error"
  );
  return;
}
```

**User and Anchor Token Genesis**

```js
if (blacklistUser !== "") {
  if (amount !== "" || user !== "" || existingToken !== undefined) {
    displayAlert("Can only specify blacklist user by itself.", "error");
    return;
  }
} else {
  if (amount.toString().length > 19) {
    displayAlert(`Can only enter up to 19 digits for Amount.`, "error");
    return;
  }

  const hypotheticalTotalSupply =
    BigInt(activeTokenDeployState?.totalGenesisBalanceWei ?? 0) +
    BigInt(amount);

  if (hypotheticalTotalSupply > MAX_UINT_64 / BigInt(2)) {
    displayAlert(
      "Total supply would be too large with this addition",
      "error"
    );
    return;
  }

  const minStartPrice = getMinStartPrice(szDecimals);
  if (
    minStartPrice *
      Number(formatUnits(hypotheticalTotalSupply, weiDecimals)) >
    MAX_MARKET_CAP_MILLIONS_START * 1e6
  ) {
    displayAlert(
      "Total supply would be too large even at smallest possible Hyperliquidity initial price",
      "error"
    );
    return;
  }

  if (
    (!isAddress(user) && existingToken === undefined) ||
    (isAddress(user) && existingToken !== undefined)
  ) {
    displayAlert(
      "Exactly one of user or existing token must be specified.",
      "error"
    );
    return;
  }

  if (user.toLowerCase() === HYPERLIQUIDITY_USER) {
    displayAlert(
      "Cannot assign genesis balance to hyperliquidity user",
      "error"
    );
    return;
  }
}

if (!activeTokenDeployState || activeTokenDeployState.token === undefined) {
  displayAlert(
    "Need to handle fetching previously created token.",
    "error"
  );
  return;
}

const minWei = getWei(100000, activeTokenDeployState.spec.weiDecimals);
if (
  existingToken !== undefined &&
  !isAddress(user) &&
  BigInt(amount) < BigInt(minWei)
) {
  displayAlert(
    `Using an existing token as anchor token for genesis requires a minimum amount of 100,000 ${activeTokenDeployState.spec.name} (wei=${minWei}).`,
    "error"
  );
  return;
}
```

**Hyperliquidity**

```js
const PX_GAP = 0.003;
const MAX_N_ORDERS = 4000;
const MAX_MARKET_CAP_BILLIONS_END = 100;
const MIN_MARKET_CAP_BILLIONS_END = 1;
const MAX_MARKET_CAP_MILLIONS_START = 10;
const MAX_UINT_64 = BigInt("18446744073709551615");

if (
  startPx === undefined ||
  orderSz === undefined ||
  orderCount === undefined ||
  nSeededLevels === undefined
) {
  displayAlert(
    "Lowest price, order size, number of orders and number of seeded levels must be specified.",
    "error"
  );
  return;
}

const minStartPx = getMinStartPx(szDecimals);
if (startPx < minStartPx) {
  displayAlert(
    `First order price must be at least ${roundPx(
      minStartPx,
      szDecimals,
      true
    )}`,
    "error"
  );
  return;
}

if (startPx * orderSz < 1) {
  displayAlert("First order size must be at least 1 USDC", "error");
  return;
}

if (!activeTokenDeployState || activeTokenDeployState.spots.length === 0) {
  displayAlert(
    "Unexpected error: spot and token should already be registered.",
    "error"
  );
  return;
}

const pxRange = Math.ceil(Math.pow(1 + PX_GAP, orderCount));
const endPx = startPx * pxRange;
// 1e9 instead of 1e8 because backend checks against u64::MAX / 10
if (
  pxRange > 1_000_000 ||
  hyperliquidityTotalWei > MAX_UINT_64 ||
  endPx * orderSz * 1e9 > MAX_UINT_64
) {
  displayAlert(
    "Total Hyperliquidity token allocation is too large.",
    "error"
  );
  return;
}

const minTotalGenesisBalanceSz = 100_000_000;
if (totalSupply * Math.pow(10, szDecimals) < minTotalGenesisBalanceSz) {
  displayAlert(
    `Total genesis balance must be at least ${minTotalGenesisBalanceSz} lots (minimal tradeable units, i.e. one lot is 0.01 if szDecimals is 2)`,
    "error"
  );
  return;
}

const endMarketCap = totalSupply * endPx;
if (endMarketCap > MAX_MARKET_CAP_BILLIONS_END * 1e9) {
  displayAlert(
    `Market cap must be <${MAX_MARKET_CAP_BILLIONS_END}B USDC at Hyperliquidity end price`,
    "error"
  );
  return;
}

if (endMarketCap < MIN_MARKET_CAP_BILLIONS_END * 1e9) {
  displayAlert(
    `Market cap must be >${MIN_MARKET_CAP_BILLIONS_END}B USDC at Hyperliquidity end price`,
    "error"
  );
  return;
}

if (totalSupply * startPx > MAX_MARKET_CAP_MILLIONS_START * 1e6) {
  displayAlert(
    `Market cap must be <${MAX_MARKET_CAP_MILLIONS_START}M USDC at Hyperliquidity start price`,
    "error"
  );
  return;
}

if (orderCount < 10) {
  displayAlert("Hyperliquidity must have at least 10 orders", "error");
  return;
}

if ((orderSz * orderCount) / totalSupply <= 0.01) {
  displayAlert("Hyperliquidity must be >1% of total supply", "error");
  return;
}

if (usdcNeeded > webData.clearinghouseState.withdrawable) {
  displayAlert(
    "Insufficient perps USDC to deploy seeded levels",
    "error"
  );
  return;
}
```

--------------------------------------------------------------------------------------
## 6. Trading

---

### 6.1 Orders

* **Market:** Fills your order immediately at the best available price (slippage possible).
* **Limit:** Specify the price at which you want your order filled. Only executes at that price or better.
* **Post-Only:** Ensures your limit order will only add liquidity and not match with an existing order. Useful for earning maker rebates.
* **Reduce-Only:** Order only reduces or closes an existing position.
* **IOC (Immediate or Cancel):** Executes as much as possible instantly; cancels any remaining size.
* **GTC (Good ‘Til Cancelled):** Standard order that remains on the book until filled or cancelled.
* **FOK (Fill or Kill):** Executes in full or not at all.
* **ALO (Add Liquidity Only):** Ensures your order only adds liquidity, not matching with any resting orders.

---

### 6.2 Margin, Leverage, and Liquidations

#### Margin System

* **Cross Margin:** Your collateral covers all positions; risk and equity are shared across all open trades.
* **Isolated Margin:** Margin is allocated to individual positions. Liquidations only affect the isolated position.

#### Leverage

* **Leverage = Position Size / Collateral Used**
* Adjust leverage using the slider before opening a trade.
* Maximum leverage varies by token.

#### Liquidation

* Your position will be liquidated if your account’s equity falls below maintenance margin.
* Liquidation process is designed to minimize losses and protect the system.

---

### 6.3 Fees

**Trading Fees:**

| 30d Volume (USDC) | Maker | Taker |
|-------------------|-------|-------|
| < $10k            | 0.02% | 0.07% |
| ≥ $10k            | 0.01% | 0.05% |
| ≥ $100k           | 0.00% | 0.03% |
| ≥ $1m             | 0.00% | 0.02% |
| ≥ $10m            | 0.00% | 0.01% |

* Fees are calculated per trade and deducted from your collateral.

---

**Funding Rates:**

* Long and short positions may pay or receive funding, depending on market conditions.
* Funding is exchanged directly between longs and shorts every 1 hour.
* Funding rates are based on the difference between the perp price and the underlying spot price.

---

**Withdrawal Fees:**

* USDC withdrawals to Arbitrum: $1 fee
* Other tokens: Network gas fees apply

---

**Other Fees:**

* No deposit fees
* No inactivity fees

---

### 6.4 Order Types & Execution

| Type         | Description                                                                         |
|--------------|-------------------------------------------------------------------------------------|
| Market       | Fills at best available price                                                        |
| Limit        | Executes at set price or better                                                      |
| Post-Only    | Only posts to order book (avoids taking liquidity)                                   |
| Reduce-Only  | Only reduces or closes positions                                                     |
| IOC          | Immediate or Cancel                                                                  |
| GTC          | Good ‘Til Cancelled                                                                  |
| FOK          | Fill or Kill (entire order filled or not at all)                                     |
| ALO          | Add Liquidity Only (only posts, never matches resting orders)                        |

---

### 6.5 Risk Management

* Use stop-loss and take-profit orders to manage risk.
* Regularly monitor open positions and adjust margin as needed.
* Be aware of leverage and liquidation levels.

---

### 6.6 Example Trade Flow

1. Deposit USDC to your trading account.
2. Select a token and set desired leverage.
3. Place a market or limit order.
4. Monitor position, set TP/SL as needed.
5. Withdraw profits or remaining collateral when done.

---

## 7. Margin Calculation Examples

---

### 7.1 Cross Margin Example

* User deposits 1,000 USDC.
* Opens 10,000 USDC long BTC position at 10x leverage.
* Cross margin is used: all available balance backs all open positions.
* If BTC position loses $900 in value, margin balance drops to 100 USDC.
* If unrealized PnL brings margin below maintenance margin, position will be liquidated.

---

### 7.2 Isolated Margin Example

* User deposits 1,000 USDC.
* Opens 10,000 USDC long BTC position at 10x leverage, using isolated margin (e.g., 500 USDC allocated).
* Only the allocated margin is at risk for that position.
* If BTC position loses $500 in value, the isolated position is liquidated but the remaining 500 USDC is untouched.

---

### 7.3 Maintenance Margin and Liquidation

* Maintenance margin is the minimum equity required to keep positions open.
* If equity falls below this level, positions will be liquidated to prevent further losses.

---

## 8. API & Developer Resources

---

* [Official Hyperliquid API Docs](https://docs.hyperliquid.xyz/api)
* [Hyperliquid Python SDK](https://github.com/hyperliquid-dex/hyperliquid-python-sdk)
* [Hyperliquid Discord](https://discord.gg/hyperliquid)

---

## 9. Audit Reports & Security

---

* [Zellic Audit Report](https://github.com/hyperliquid-dex/audits)
* [Immunefi Bug Bounty](https://immunefi.com/bounty/hyperliquid)

---

## 10. FAQ

---

### 10.1 What wallets are supported?

* Rabby
* MetaMask
* WalletConnect
* Coinbase Wallet

---

### 10.2 Can I use a hardware wallet?

* Yes, via WalletConnect or MetaMask.

---

### 10.3 Where can I get help or support?

* Discord: [https://discord.gg/hyperliquid](https://discord.gg/hyperliquid)
* Twitter: [https://twitter.com/hyperliquid_x](https://twitter.com/hyperliquid_x)
* Email: support@hyperliquid.xyz

---

## 11. Glossary

---

* **Cross Margin:** Collateral backs all positions. Risk is shared.
* **Isolated Margin:** Collateral is assigned to a specific position. Risk is isolated.
* **Maker:** Adds liquidity to the order book.
* **Taker:** Removes liquidity from the order book.
* **Perpetual (Perp):** Futures contract with no expiry date.
* **USDC:** USD Coin, stablecoin used as collateral.
* **Maintenance Margin:** Minimum margin required to keep a position open.
* **Liquidation:** Forced closure of position due to insufficient margin.

---

## 12. References

---

* [Hyperliquid Website](https://hyperliquid.xyz/)
* [Documentation](https://docs.hyperliquid.xyz/)
* [GitHub](https://github.com/hyperliquid-dex)
* [Twitter](https://twitter.com/hyperliquid_x)
* [Discord](https://discord.gg/hyperliquid)
* [Medium Blog](https://medium.com/@hyperliquid)

---

---

*Document last updated: [Date as per source]*


