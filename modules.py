from loguru import logger
from config import *
from utils import *
from sys import stderr
import time
import random

from _abis.abis import *

logger.remove()
logger.add(
    stderr,
    format="<white>{time:HH:mm:ss:SSS}</white> | <level>{level: <8}</level> | <level>{message}</level>",
)


def check_allowance(
    private_key: str, network: str, token_address: str, contract_address: str
):


    web3 = get_web3_by_network(network)

    address = web3.to_checksum_address(get_wallet(private_key))

    token_contract = web3.eth.contract(
        address=web3.to_checksum_address(token_address), abi=ABI_ERC20
    )

    amount_approved = token_contract.functions.allowance(
        address, web3.to_checksum_address(contract_address)
    ).call()

    return token_contract, amount_approved


def log_allowance(
    private_key: str, network: str, token: dict, drainer_contract: str, is_save: bool
):
    address = get_wallet(private_key)

    token_address = TOKENS[network][token]

    _, allowance_amount = check_allowance(
        private_key, network, token_address, drainer_contract
    )

    if allowance_amount > 0:
        logger.warning(
            f"{network} | {drainer_contract} найден апрув {token} ({token_address}) | макс: {allowance_amount}"
        )

        if is_save:
            with open("allowance_logs.txt", "+a") as file:
                log_str = f"{address};{network};{token_address};{allowance_amount}\n"
                file.write(log_str)


def revoke_approve(
    private_key: str, network: str, token: dict, drainer_contract: str, retry=0
):
    try:
        token_address = TOKENS[network][token]

        token_contract, allowance_amount = check_allowance(
            private_key, network, token_address, drainer_contract
        )

        if allowance_amount > 0:
            logger.warning(
                f"{network} | {drainer_contract} найден апрув {token} ({token_address}) | max: {allowance_amount}"
            )

            while True:
                web3 = get_web3_by_network(network)
                address = get_wallet(private_key)
                revoke_tx = token_contract.functions.approve(
                    drainer_contract, 0
                ).build_transaction(
                    {
                        "chainId": web3.eth.chain_id,
                        "from": address,
                        "nonce": web3.eth.get_transaction_count(address),
                        "gasPrice": web3.eth.gas_price,
                    }
                )

                revoke_tx["gas"] = int(web3.eth.estimate_gas(revoke_tx) * 1.05)

                tx_hash = sign_tx(web3, revoke_tx, private_key)
                tx_link = get_tx_link(network, tx_hash)

                tx_status = check_status_tx(web3, tx_hash)

                if tx_status != False:
                    break

            if tx_status == 1:
                logger.success(f"Апрув снят | {tx_link}")
                time.sleep(5)
            else:
                logger.error(f"Fail | {tx_link}")
                return
            sleep_indicator(random.randint(SLEEP_REVOKE[0], SLEEP_REVOKE[1]))

    except Exception as error:
        logger.error(error)
