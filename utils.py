from web3 import HTTPProvider, Web3

from _abis.abis import *
from loguru import logger
import time
from config import *
from tqdm import tqdm


def gas_price_chk():
    web3 = Web3(HTTPProvider(DATA["ethereum"]["rpc"]))
    while True:
        if web3.is_connected():
            break
        else:
            logger.info(f'Not connect to RPC')
            time.sleep(5)
    while True:
        try:
            current_gas_price = web3.eth.gas_price
            current_gas_price_gwei = web3.from_wei(current_gas_price, 'gwei')
            if round(current_gas_price_gwei, 1) <= Gwei:
                break
            else:
                logger.info(f'GWEI {round(current_gas_price_gwei, 1)}  Ждем Gwei ниже {Gwei}. Сплю 30 секунд')
                time.sleep(30)
        except Exception as err:
            logger.info(err)


def sleep_indicator(sec):
    for i in tqdm(range(sec), desc='Пауза', bar_format="{desc}: {n_fmt}c /{total_fmt}c {bar}", colour='green'):
        time.sleep(1)

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
                tx_hash, timeout=2000
            ).status
            return tx_status
        except Exception as e:
            None
