class NetworkConnection:
    """네트워크 연결을 나타내는 클래스"""

    def __init__(self, url):
        """인스턴스를 초기화한다."""

        self.url = url
        self.is_connected = False

    def connect(self):
        """네트워크에 연결한다."""

        print('네트워크에 연결합니다.')
        self.is_connected = True

    def disconnect(self):
        """네트워크 연결을 중단한다."""

        print('네트워크 연결을 중단합니다.')
        self.is_connected = False

    def read(self):
        """네트워크에서 데이터를 읽어 들인다."""

        return '네트워크에서 읽어 들인 데이터'

    def __enter__(self):
        """객체 사용을 준비한다."""

        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """객체 사용을 마치고 뒷정리한다."""

        self.disconnect()


with NetworkConnection('https://bakyeono.net') as connection:
    print(connection.read())