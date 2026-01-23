from abc import ABC, abstractmethod
from dataclasses import dataclass
from account import Account

@dataclass
class CurrentAccount(Account):
    overdraft_Limit: float = 500.0

    def withdraw(self, amount):
        if amount > self._balance + self.overdraft_Limit:
            raise ValueError("Withdrawal exceeds overdraft limit")
        self._balance -= amount
    