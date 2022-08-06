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

