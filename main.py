from modules import *
from config import *
import random

if __name__ == "__main__":
    try:
        SAVE_IN_FILE = False

        print("Режим работы?\n\t1. Проверка наличия апрува\n\t2. Снятие апрува")
        picked_func = input("> ")

        if picked_func == "1":
            print("Сохранить результат работы в allowance_logs.txt?\n\t1. Yes\n\t2. No")
            is_save = input("> ")
            if is_save == "1":
                SAVE_IN_FILE = True
            else:
                pass

        if SHUFFLE_PRIVATE:
            random.shuffle(PRIVATE_KEYS)

        for private_key in PRIVATE_KEYS:
            address = get_wallet(private_key)
            logger.info(address)
            for network in NEED_REVOKE_CONTRACTS:
                for drainer_contract in NEED_REVOKE_CONTRACTS[network]:
                    for token in TOKENS[network]:
                        if picked_func == "1":
                            try:
                                log_allowance(
                                    private_key,
                                    network,
                                    token,
                                    drainer_contract,
                                    SAVE_IN_FILE,
                                )
                            except Exception as err:
                                print(err)
                            time.sleep(SLEEP_CHK_ALLOW)
                        elif picked_func == "2":
                            gas_price_chk()     # Газ чек
                            revoke_approve(
                                private_key, network, token, drainer_contract
                            )
                        else:
                            break
            sleep_indicator(random.randint(SLEEP_WALL[0], SLEEP_WALL[1]))
    except KeyboardInterrupt:
        print()
        logger.success(f"Instantly exited.")
