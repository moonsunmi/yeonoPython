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

        if self.is_frozen:
            raise FrozenAccountException

        if not amount > 0:
            raise InvalidTransactionException('0 이하의 액수는 입금할 수 없습니다.')

        self.balance += amount

    def withdraw(self, amount):
        """계좌에서 amount만큼의 금액을 인출한다."""
        if self.is_frozen:
            raise FrozenAccountException

        if not amount > 0:
            raise InvalidTransactionException('0 이하의 액수는 인출할 수 없습니다.')

        if self.balance < amount:
            raise AccountBalanceException('잔액이 부족합니다.')
        else:
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