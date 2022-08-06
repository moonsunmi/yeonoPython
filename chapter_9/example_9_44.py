class DoorException(Exception):
    """문 관련 예외"""
    pass
class DoorOpenedException(DoorException):
    """문 열림 예외"""
    pass
class DoorClosedException(DoorException):
    """문 닫힘 예외"""
    pass

class Door:
    """문을 나타내는 클래스"""
    def __init__(self):
        self._is_opened = True

    def open(self):
        assert not self._is_opened

        print('문을 엽니다.')
        self._is_opened = True

    def close(self):
        assert self._is_opened

        print('문을 닫습니다.')
        self._is_opened = False

door = Door()
door.close()
door.open()
door.open()