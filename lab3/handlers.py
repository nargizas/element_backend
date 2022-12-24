from typing import Optional
from Models.Account import Account
from Models.BankAccount import BankAccount
from services import BankAccountServices


class BankAccountHandlers:

    services: BankAccountServices

    def __init__(self, services: BankAccountServices) -> None:
        self.services = services

    def create_bank_account(self, name: str, surname: str, account: str) -> None:
        name = name.strip()
        surname = surname.strip()
        account_type = Account.KZT
        match account:
            case "USD":
                account_type = Account.USD
            case "1":
                account_type = Account.USD
            case "RUB":
                account_type = Account.RUB
            case "2":
                account_type = Account.RUB
            case "KZT":
                account_type = Account.KZT
            case "3":
                account_type = Account.KZT
            case "EUR":
                account_type = Account.EUR
            case "4":
                account_type = Account.EUR
            case _:
                print("Неправильный ввод")
                return

        self.services.create_bank_account(
            name=name, surname=surname, account=account_type
        )

    def get_bank_account(
        self, name: str, surname: str, account: Account
    ) -> Optional[BankAccount]:
        name = name.strip()
        surname = surname.strip()
        account_type = Account.KZT
        match account:
            case "USD":
                account_type = Account.USD
            case "1":
                account_type = Account.USD
            case "RUB":
                account_type = Account.RUB
            case "2":
                account_type = Account.RUB
            case "KZT":
                account_type = Account.KZT
            case "3":
                account_type = Account.KZT
            case "EUR":
                account_type = Account.EUR
            case "4":
                account_type = Account.EUR
            case _:
                print("Неправильный ввод")
                return

        return self.services.get_bank_account(
            name=name, surname=surname, account=account_type
        )

    def add_to_bank_account(self, bank_account: BankAccount, added_amount: str) -> None:
        if not added_amount.isnumeric():
            print("Введите число")
            return
        added_amount = float(added_amount)
        self.services.add_to_bank_account(bank_account=bank_account, x=added_amount)

    def subtract_from_bank_account(
        self, bank_account: BankAccount, subtracted_amount: str
    ) -> None:
        if not subtracted_amount.isnumeric():
            print("Введите число")
            return
        subtracted_amount = float(subtracted_amount)
        self.services.subtract_from_bank_account(
            bank_account=bank_account, x=subtracted_amount
        )

    def money_conversion(
        self, bank_account: BankAccount, target_currency: str
    ) -> float:
        match target_currency:
            case "USD":
                target = Account.USD
            case "1":
                target = Account.USD
            case "RUB":
                target = Account.RUB
            case "2":
                target = Account.RUB
            case "KZT":
                target = Account.KZT
            case "3":
                target = Account.KZT
            case "EUR":
                target = Account.EUR
            case "4":
                target = Account.EUR
            case _:
                print("Неправильный ввод")
                return

        return self.services.money_conversion(
            bank_account=bank_account, target_currency=target
        )
