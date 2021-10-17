class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.balance = balance

    def _check(self, account, money):
        if account <= 0 or account > self.n:
            return False
        if self.balance[account - 1] < money:
            return False
        return True

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self._check(account1, money):
            return False
        if not self._check(account2, 0):
            return False
        self.balance[account1-1] -= money
        self.balance[account2-1] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if not self._check(account, 0):
            return False
        self.balance[account-1] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if not self._check(account, money):
            return False
        self.balance[account-1] -= money
        return True
