from account import Account
from dataclasses import dataclass

@dataclass
class SavingsAccount(Account):
    interest_rate: float = 0.02

    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def add_interest(self):
        self._balance += self._balance * self.interest_rate
       