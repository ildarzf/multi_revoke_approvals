from modules import *
from config import *

if __name__ == "__main__":
    try:
        SAVE_IN_FILE = False

        print("How we are working?\n\t1. Approval check\n\t2. Remove approvals")
        picked_func = input("> ")

        if picked_func == "1":
            print("Save logs?\n\t1. Yes\n\t2. No")
            is_save = input("> ")
            if is_save == "1":
                SAVE_IN_FILE = True
            else:
                pass

        for private_key in PRIVATE_KEYS:
            address = get_wallet(private_key)
            logger.info(address)

            for network in NEED_REVOKE_CONTRACTS:
                for drainer_contract in NEED_REVOKE_CONTRACTS[network]:
                    for token in TOKENS[network]:
                        if picked_func == "1":
                            log_allowance(
                                private_key,
                                network,
                                token,
                                drainer_contract,
                                SAVE_IN_FILE,
                            )
                        elif picked_func == "2":
                            revoke_approve(
                                private_key, network, token, drainer_contract
                            )
                        else:
                            break

    except KeyboardInterrupt:
        print()
        logger.success(f"Instantly exited.")
