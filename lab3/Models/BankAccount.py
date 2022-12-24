from Models.Account import Account


class BankAccount:
    name: str
    surname: str
    _balance: float
    account: Account

    def __init__(self, name: str, surname: str, account: Account) -> None:
        self.name = name
        self.surname = surname
        self.account = account
        self._balance = 0

    def add_to_bank_account(self, x: float):
        self._balance += x

    def subtract_from_bank_account(self, x: float):
        if self._balance < x:
            print("Non sufficient funds")
        else:
            self._balance -= x

    def get_balance(self):
        return self._balance

    def set_balance(self, x: float):
        self._balance = x

    def money_conversion(self, target_currency) -> float:
        match self.account:
            case Account.USD:
                match target_currency:
                    case Account.KZT:
                        self._balance = self._balance * 468
                        self.account = Account.KZT
                    case Account.EUR:
                        self._balance = self._balance * 0.94
                        self.account = Account.EUR
                    case Account.RUB:
                        self._balance = self._balance * 72
                        self.account = Account.RUB
            case Account.KZT:
                match target_currency:
                    case Account.USD:
                        self._balance = self._balance / 468
                        self.account = Account.USD
                    case Account.EUR:
                        self._balance = self._balance / 498.1
                        self.account = Account.EUR
                    case Account.RUB:
                        self._balance = self._balance * 0.15
                        self.account = Account.RUB
            case Account.EUR:
                match target_currency:
                    case Account.KZT:
                        self._balance = self._balance * 498.1
                        self.account = Account.KZT
                    case Account.USD:
                        self._balance = self._balance * 0.94
                        self.account = Account.USD
                    case Account.RUB:
                        self._balance = self._balance * 76.58
                        self.account = Account.RUB
            case Account.RUB:
                match target_currency:
                    case Account.KZT:
                        self._balance = self._balance / 0.15
                        self.account = Account.KZT
                    case Account.USD:
                        self._balance = self._balance / 72
                        self.account = Account.USD
                    case Account.EUR:
                        self._balance = self._balance / 76.58
                        self.account = Account.EUR

        # print(self._balance)
        print(f"Your current balance is {self._balance} {self.account.value}")
        return self._balance

    def __repr__(self) -> str:
        return f"You are {self.name} {self.surname}. Your current balance is {self._balance}. Your account type is {self.account.value}."

    def __del__(self):
        print("Your account has been deleted")
