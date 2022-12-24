from typing import Optional
from Models.Account import Account
from Models.BankAccount import BankAccount


class BankAccountRepositories:
    bank_accounts: list[BankAccount] = []

    def create_bank_account(self, name: str, surname: str, account: Account) -> None:
        new_bank_account = BankAccount(name, surname, account)
        self.bank_accounts.append(new_bank_account)
        # print(self.bank_accounts)

    def get_bank_account(
        self, name: str, surname: str, account: Account
    ) -> Optional[BankAccount]:
        b_account = next(
            (
                u
                for u in self.bank_accounts
                if name == u.name and surname == u.surname and account == u.account
            ),
            None,
        )

        if not b_account:
            print("Account not found")
            return
        return b_account

    def delete_account(self, name: str, surname: str, account: Account) -> None:
        b_account = next(
            (
                u
                for u in self.bank_accounts
                if name == u.name and surname == u.surname and account == u.account
            ),
            None,
        )

        if not b_account:
            print("Account not found")
            return

        self.bank_accounts.remove(b_account)
