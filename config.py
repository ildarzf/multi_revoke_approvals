TOKENS = {
    "ethereum": {
        "USDT": "0xdac17f958d2ee523a2206206994597c13d831ec7",
        "USDC": "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48",
    },
    "optimism": {
        "USDT": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58",
        "USDC": "0x7f5c764cbc14f9669b88837ca1490cca17c31607",
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
    },
    "avalanche": {
        "USDT": "0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",
        "USDC": "0xB97EF9Ef8734C71904D8002F8b6Bc66Dd9c48a6E",
        "USDC.e": "0xa7d7079b0fead91f3e65f86e8915cb59c1a4c664",
    },
}

NEED_REVOKE_CONTRACTS = {
    "ethereum": [
        "0x32c85e56A82d66Fa3C13E7dF900682D63fcBAf89",
        "0x79cdFd7Bc46D577b95ed92bcdc8abAba1844Af0c",
    ],
    "optimism": ["0xFb1b9A97f1836173390D8bdEaF9004727311A8e1"],
    "bsc": [
        "0x375E05F6e12028e933ce598Ad1BEd7f1194aB071",
        "0x3Fff9A58676584bA28E8780366d7D9CEf0EB78ce",
    ],
    "polygon": [
        "0xACfaAa9Da11e66a8Cc8AF8E3D844673968FFf63f",
        "0x8Ee11bBD4139989e5F8BB92E8a9E01BC08DF3011",
    ],
    "arbitrum": [
        "0x36c543B8bb76b330ecB66A13c1C1377f889f1919",
        "0x6fcE1a7c3347E78D22C278eB3a5c72Ec8FcEa294",
    ],
    "avalanche": [
        "0x43B4bf8758CAE65E6b8242D2669E0E5E20Ff693A",
        "0x45E817D12758aC37BC8DD3C71143c1bE75e3eD6F",
    ],
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
}

with open("private_keys.txt", "r") as f:
    PRIVATE_KEYS = [row.strip() for row in f]
