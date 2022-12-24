from typing import Optional
from Models.Account import Account
from Models.BankAccount import BankAccount
from repositories import BankAccountRepositories


class BankAccountServices:

    repos: BankAccountRepositories

    def __init__(self, repos: BankAccountRepositories) -> None:
        self.repos = repos

    def create_bank_account(self, name: str, surname: str, account: Account) -> None:
        self.repos.create_bank_account(name=name, surname=surname, account=account)

    def get_bank_account(
        self, name: str, surname: str, account: Account
    ) -> Optional[BankAccount]:
        return self.repos.get_bank_account(name=name, surname=surname, account=account)

    def add_to_bank_account(self, bank_account: BankAccount, x: float) -> None:
        bank_account.add_to_bank_account(x)

    def subtract_from_bank_account(self, bank_account: BankAccount, x: float) -> None:
        bank_account.subtract_from_bank_account(x)

    def money_conversion(
        self, bank_account: BankAccount, target_currency: Account
    ) -> float:
        return bank_account.money_conversion(target_currency=target_currency)
