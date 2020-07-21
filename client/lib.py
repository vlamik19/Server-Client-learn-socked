import socket
from time import strftime


class Client(object):
    def __init__(self, ip: str, port: int, login: str, win):
        super().__init__()
        self._ip = ip
        self._port = port
        self._login = login
        self._win = win
        self._listener = None

    def start(self):
        try:
            message = self._win.ui.lineEdit_4.text()
            self._listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._listener.connect((self._ip, self._port))
            self._listener.send(message.encode(encoding="utf-8"))
            self._listener.close()
        except BaseException as err:
            print(err)
















