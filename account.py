from abc import ABC, abstractmethod
from dataclasses import dataclass
@dataclass
class Account(ABC):
        account_holder: str  
        account_number: int
        _balance: float


        def deposit(self, amount: float):
            if amount < 0:
                raise ValueError("Deposit amount must be positive")
            self._balance += amount

        @abstractmethod
        def withdraw(self, amount: float):
            pass

        def get_balance(self):
            return self._balance