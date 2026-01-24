from account import Account
from dataclasses import dataclass

# Define a SavingsAccount class that inherits from Account
@dataclass
class SavingsAccount(Account):
    interest_rate: float = 0.02

# Implement the withdraw method (polymorphism)
    def withdraw(self, amount: float):
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
        
# Implement a method to add interest to the balance
    def add_interest(self):
        self._balance += self._balance * self.interest_rate
       