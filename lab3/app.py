import sys
from handlers import BankAccountHandlers
from repositories import BankAccountRepositories
from services import BankAccountServices


def init():
    bank_account_repositories = BankAccountRepositories()
    bank_account_services = BankAccountServices(repos=bank_account_repositories)
    bank_account_handlers = BankAccountHandlers(services=bank_account_services)

    while True:
        command = input(
            """
        Выберите номер вашего действия:
        1. Создать банковский аккаунт
        2. Выбрать банковский аккаунт
        0. Выйти
        """
        )

        match command:
            case "1":
                name = input("Введите ваше имя: ")
                surname = input("Введите вашу фамилию: ")
                account = input(
                    """
                Выберите валюту:
                1. USD
                2. RUB
                3. KZT
                4. EUR
                """
                )
                bank_account_handlers.create_bank_account(
                    name=name, surname=surname, account=account
                )
            case "2":
                name = input("Введите ваше имя: ")
                surname = input("Введите вашу фамилию: ")
                account = input(
                    """
                Выберите валюту:
                1. USD
                2. RUB
                3. KZT
                4. EUR
                """
                )
                bank_account = bank_account_handlers.get_bank_account(
                    name=name, surname=surname, account=account
                )
                print(bank_account)
                while True:
                    action = input(
                        """
                    Выберите номер вашего действия:
                    1. Положить деньги на банковский аккаунт
                    2. Снять деньги с банковского аккаунта
                    3. Перевести деньги на другую валюту
                    4. Просмотреть информацию про ваш банковский аккаунт
                    5. Назад
                    0. Выйти
                    """
                    )
                    match action:
                        case "1":
                            amount = input("Введите сумму:")
                            bank_account_handlers.add_to_bank_account(
                                bank_account=bank_account, added_amount=amount
                            )
                        case "2":
                            amount = input("Введите сумму:")
                            bank_account_handlers.subtract_from_bank_account(
                                bank_account=bank_account, subtracted_amount=amount
                            )
                        case "3":
                            target_currency = input(
                                """
                                Выберите валюту:
                                1. USD
                                2. RUB
                                3. KZT
                                4. EUR
                                """
                            )
                            bank_account_handlers.money_conversion(
                                bank_account=bank_account,
                                target_currency=target_currency,
                            )

                        case "4":
                            print(bank_account)
                        case "5":
                            break
                        case "0":
                            sys.exit(0)
                        case _:
                            print("Выберите из перечисленных действий")
            case "0":
                sys.exit(0)
            case _:
                print("Выберите из перечисленных действий")


if __name__ == "__main__":
    init()
