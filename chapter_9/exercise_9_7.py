class AccountException(Exception):
    """은행 계좌 관련 예외"""
    pass

class AccountBalanceException(AccountException):
    """계좌 잔고 예외"""
    pass

class FrozenAccountException(AccountException):
    """동결 계좌 예외"""
    pass

class InvalidTransactionException(AccountException):
    """잘못된 입출금 예외"""
    pass


class Account():
    """은행 계좌"""

    def __init__(self, balance, is_frozen):
        """인스턴스를 초기화한다."""
        self.balance = balance  # 계좌 잔액
        self.is_frozen = is_frozen  # 계좌 동결 여부

    def check(self):
        """계좌의 잔고를 조회한다."""

        print('계좌 잔액은', self.balance, '원입니다.')

    def deposit(self, amount):
        """계좌에 amount만큼의 금액을 입금한다."""

        assert amount > 0, '거래 금액이 잘못되었습니다.'

        self.balance += amount

    def withdraw(self, amount):
        """계좌에서 amount만큼의 금액을 인출한다."""
        assert not self.is_frozen, '계좌가 동결되었습니다.'
        assert amount > 0, '거래 금액이 잘못되었습니다.'
        assert self.balance >= amount, '잔액이 부족합니다.'

        self.balance -= amount


account_1 = Account(1000, False)

try:
    account_1.deposit(1000)
except Exception as error:
    print(error)

try:
    account_1.withdraw(-1000)
except Exception as error:
    print(error)

try:
    account_1.check()
except Exception as error:
    print(error)