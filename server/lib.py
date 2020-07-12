import socket
from threading import Thread
from time import strftime


class Server(object):

    def __init__(self, ip: str, port: int, win):
        super().__init__()
        self._ip = ip
        self._port = port
        self._win = win
        self._listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._stop_flag = False

    def start(self) -> None:
        try:
            self._listener.bind((self._ip, self._port))
            self._listener.listen(10)
            current_time = strftime('%d.%m.%Y %H:%M:%S')
            self._win.ui.textEdit.append(f'{current_time} -> Сервер включен!')

            server_thread = Threads(self._listener, self._win, self._stop_flag)
            server_thread.setDaemon(True)
            server_thread.start()
        except BaseException as err:
            print(err)

    def stop(self) -> None:
        self._stop_flag = True
        current_time = strftime('%d.%m.%Y %H:%M:%S')
        self._win.ui.textEdit.append(f'{current_time} -> Сервер выключен!')


class Threads(Thread):

    def __init__(self, listener, win, stop_flag):
        super().__init__()
        self._listener = listener
        self._win = win
        self._stop_flag = stop_flag

    def run(self) -> None:
        while True:
            if not self._stop_flag:
                current_time = strftime('%d.%m.%Y %H:%M:%S')
                self._win.ui.textEdit.append(f'{current_time} -> Ожидание запросов ...')
                connection, client_address = self._listener.accept()
                client_message = connection.recv(1024).decode(encoding='utf-8')

                if client_message == 'GET_CHAT':
                    connection.send(self._win.ui.textEdit.toPlainText().encode(encoding='utf-8'))
                else:
                    current_time = strftime('%d.%m.%Y %H:%M:%S')
                    self._win.ui.textEdit.append(f'{current_time} -> {client_address} :: {client_message}\n')
                connection.close()
            else:
                break


