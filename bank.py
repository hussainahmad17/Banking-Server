class Bank:
    def __init__(self, name):
        self._name = name
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)
    
    def close_account(self, account):
        self._accounts.remove(account)

    def find_account(self, account_number):
        for account in self._accounts:
            if account.account_number == account_number:
                return account
            
    def total_balance(self):
        return sum(account.balance for account in self._accounts)