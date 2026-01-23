from bank import Bank
from savings_account import SavingsAccount

from current_account import CurrentAccount

def main():
    bank = Bank("Smart Bank")

    savings = SavingsAccount("Ali",101, 5000)
    current = CurrentAccount("Ahmed", 102, 2000)

    bank.add_account(savings)
    bank.add_account(current)

    savings.deposit(1000)
    savings.withdraw(200)
    savings.add_interest()

    current.withdraw(3000)

    print("Savings Account Balance:", savings.get_balance())
    print("Current Account Balance:", current.get_balance())
    print("Total Bank Balance:", bank.total_bank_balance())

if __name__ == "__main__":
    main()
