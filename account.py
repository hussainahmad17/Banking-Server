from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_holder, account_number, balance):
        self._account_holder = account_holder
        self._account_number = account_number
        self._balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount must be positive")
        self._balance += amount

    @abstractmethod
    def withdraw(self, amount):
        pass

    def get_balance(self):
        return self._balance