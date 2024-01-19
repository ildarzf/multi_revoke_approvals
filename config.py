Gwei = 40
SHUFFLE_PRIVATE = True  # перемешать приватники
SLEEP_WALL = [400, 1000] # спим между кошельками
SLEEP_REVOKE = [20, 50] # спим между кошельками в случае ревоука
SLEEP_CHK_ALLOW = 0.2 # задержка между кошельками на наличие апрува
UNLIM = 1000000 # смотрим и отменяем только контракты с апрувом выше 10 баксов USDC
TOKENS = {
    "ethereum": {
        "USDT": "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "USDC": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    },
    "optimism": {
        "USDT": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58",
        "USDC": "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
          "OP": "0x4200000000000000000000000000000000000042",
    },
    "bsc": {
        "USDT": "0x55d398326f99059ff775485246999027b3197955",
        "USDC": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
        "BUSD": "0xe9e7CEA3DedcA5984780Bafc599bD69ADd087D56",
    },
    "polygon": {
        "USDT": "0xc2132d05d31c914a87c6611c10748aeb04b58e8f",
        "USDC": "0x2791bca1f2de4661ed88a30c99a7a9449aa84174",
    },
    "arbitrum": {
        "USDT": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "USDC": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "USDC.e": "0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8",
        "ARB": "0x912CE59144191C1204E64559FE8253a0e49E6548",
    },
    "avalanche": {
        "USDT": "0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",
        "USDC": "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E",
        "USDC.e": "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664",
    },
    "zksync": {
        "USDC": "0x3355df6d4c9c3035724fd0e3914de96a5a83aaf4",
    },
    "scroll": {
        "USDT": "0xf55BEC9cafDbE8730f096Aa55dad6D22d44099Df",
        "USDC": "0x06eFdBFf2a14a7c8E15944D1F4A48F9F95F663A4",
    },
    "base": {
        "USDC": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
    },
    "fantom": {
        "USDC": "0x04068DA6C83AFCFA0e13ba15A6696662335D5B75",
    },


}

NEED_REVOKE_CONTRACTS = {
    "ethereum": [
        "0x8731d54E9D02c286767d56ac03e8037C07e01e98",    #bungee hack 16/01/24
    ],
    "optimism": [
        "0xB0D502E938ed5f4df2E681fE6E419ff29631d62b",
        "0x000000000022D473030F116dDEE9F6B43aC78BA3",
        "0x5130f6cE257B8F9bF7fac0A0b519Bd588120ed40",
    ],
    "bsc": [
        "0x4a364f8c717cAAD9A442737Eb7b8A55cc6cf18D8",
        "0x1a1ec25DC08e98e5E93F1104B5e5cdD298707d31",
        "0xb278163B1D2Da632D51190001BBb95d45C3b191a",
    ],
    "polygon": [
        "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd",
        "0x8Ee11bBD4139989e5F8BB92E8a9E01BC08DF3011",
    ],
    "arbitrum": [
        "0x53Bf833A5d6c4ddA888F69c22C88C9f356a41614",
    ],
    "avalanche": [
        "0x45A01E4e04F14f7A4a6702c74187c5F6222033cd",
    ],
    "fantom": [
        "0xAf5191B0De278C7286d6C7CC6ab6BB8A73bA2Cd6",
    ],
    "zksync": [
        "0xbE7D1FD1f6748bbDefC4fbaCafBb11C6Fc506d1d"
    ],
    # "scroll": [
    #     "",
    # ],
    # "base": [
    #     "0x45f1A95A4D3f3836523F5c83673c797f4d4d263B",
    # ],
}

# ===========================================================

DATA = {
    "ethereum": {
        "chain": "ETH",
        "chain_id": 1,
        "rpc": "https://rpc.ankr.com/eth",
        "scan": "https://etherscan.io/tx",
        "token": "ETH",
        "decimals": 6,
    },
    "optimism": {
        "chain": "OPTIMISM",
        "chain_id": 10,
        "rpc": "https://rpc.ankr.com/optimism",
        "scan": "https://optimistic.etherscan.io/tx",
        "token": "ETH",
        "decimals": 6,
    },
    "bsc": {
        "chain": "BNB",
        "chain_id": 56,
        "rpc": "https://rpc.ankr.com/bsc",
        "scan": "https://bscscan.com/tx",
        "token": "BNB",
        "decimals": 18,
    },
    "polygon": {
        "chain": "MATIC",
        "chain_id": 137,
        "rpc": "https://polygon-rpc.com",
        "scan": "https://polygonscan.com/tx",
        "token": "MATIC",
        "decimals": 6,
    },
    "arbitrum": {
        "chain": "ARBITRUM",
        "chain_id": 42161,
        "rpc": "https://rpc.ankr.com/arbitrum",
        "scan": "https://arbiscan.io/tx",
        "token": "ETH",
        "decimals": 6,
    },
    "avalanche": {
        "chain": "AVAXC",
        "chain_id": 43114,
        "rpc": "https://rpc.ankr.com/avalanche",
        "scan": "https://snowtrace.io/tx",
        "token": "AVAX",
        "decimals": 6,
    },
    "fantom": {
        "chain": "FTM",
        "chain_id": 250,
        "rpc": "https://rpc.ankr.com/fantom",
        "scan": "https://ftmscan.com/tx",
        "token": "FTM",
        "decimals": 6,
    },
    "zksync": {
        "chain": "zkSync",
        "chain_id": 324,
        "rpc": "https://1rpc.io/zksync2-era",
        "scan": "https://explorer.zksync.io/tx",
        "token": "ETH",
        "decimals": 6,
    },
    "scroll": {
        "chain": "SCROLL",
        "chain_id": 534352,
        "rpc": "https://rpc.ankr.com/scroll",
        "scan": "https://blockscout.scroll.io/tx",
        "token": "ETH",
        "decimals": 6,
    },
    "base": {
        "chain": "BASE",
        "chain_id": 8453,
        "rpc": "https://1rpc.io/base",
        "scan": "https://basescan.org/tx",
        "token": "ETH",
        "decimals": 6,
    },
}

with open("private_keys.txt", "r") as f:
    PRIVATE_KEYS = [row.strip() for row in f]
