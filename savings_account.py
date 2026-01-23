from account import Account
from dataclasses import dataclass

@dataclass
class SavingsAccount(Account):
    interest_rate: float = 0.02 

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount

    def add_interest(self):
        interest = self._balance * self.interest_rate
        self._balance += interest