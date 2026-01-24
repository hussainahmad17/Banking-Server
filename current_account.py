from dataclasses import dataclass
from account import Account

# Define a CurrentAccount class that inherits from Account
@dataclass
class CurrentAccount(Account):
    overdraft_Limit: float = 500.0

# Implement the withdraw method (polymorphism)
    def withdraw(self, amount: float):
        if amount > self._balance + self.overdraft_Limit:
            raise ValueError("Withdrawal exceeds overdraft limit")
        self._balance -= amount
    