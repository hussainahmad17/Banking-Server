from bank import Bank
from savings_account import SavingsAccount

from current_account import CurrentAccount

def main():
    bank = Bank("Smart Bank")

    # Create instances of SavingsAccount and CurrentAccount
    savings = SavingsAccount("Ali",101, 5000)
    current = CurrentAccount("Ahmed", 102, 2000)

    # Add accounts to the bank
    bank.add_account(savings)
    bank.add_account(current)

    # Perform some operations
    savings.deposit(1000)
    savings.withdraw(200)
    savings.add_interest()

    current.withdraw(1000)

    # find bank account with bank account number
    account = bank.find_account(101)
    if account: 
        print(f"Account found: {account.account_holder}, Balance: {account.get_balance()}")
    else:
        print("Account not found.")
        

    # Display balances
    print("Savings Account Balance:", savings.get_balance())
    print("Current Account Balance:", current.get_balance())
    print("Total Bank Balance:", bank.total_balance())

if __name__ == "__main__":
    main()
