class BankAccount:
    def __init__(self, account_number, initial_balance):
        self.__account_number = account_number
        self.__initial_balance = initial_balance

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.__initial_balance += amount
        else:
            raise ValueError('Cannot deposit zero or negative funds')

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__initial_balance:
                self.__initial_balance -= amount
            else:
                raise ValueError('Insufficient funds')
        else:
            raise ValueError('Cannot withdraw zero or negative funds')
