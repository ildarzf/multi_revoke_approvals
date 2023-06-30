from web3 import HTTPProvider, Web3

from _abis.abis import *
from config import *


def get_web3_by_network(network: str):
    return Web3(Web3.HTTPProvider(DATA[network]["rpc"]))


def get_wallet(private_key: str):
    web3 = Web3(HTTPProvider(DATA["ethereum"]["rpc"]))
    wallet = web3.eth.account.from_key(private_key).address
    return wallet


def sign_tx(web3: object, contract_txn: list, private_key: str):
    signed_tx = web3.eth.account.sign_transaction(contract_txn, private_key)
    raw_tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    tx_hash = web3.to_hex(raw_tx_hash)
    return tx_hash


def get_tx_link(network: str, tx_hash: str):
    return f"{DATA[network]['scan']}/{tx_hash}"


def check_status_tx(web3: object, tx_hash: str):
    while True:
        try:
            tx_status = web3.eth.wait_for_transaction_receipt(
                tx_hash, timeout=7200
            ).status
            return tx_status
        except Exception as e:
            None
