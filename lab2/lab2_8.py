account = 0


def addToBankAccount(x):
    account += x
    return account


def substractFromBankAccount(x):
    account -= x
    return account


def moneyConversion(x, currency1, currency2):
    if currency1 == 'USD' and currency2 == 'KZT':
        account *= 470
    elif currency1 == 'KZT' and currency2 == 'USD':
        account /= 470
    return account
