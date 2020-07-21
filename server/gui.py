from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from server.lib import Server


class ServerWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('server.ui')
        self._server = None
        self._ui.pushButton.clicked.connect(self.start)
        self._ui.pushButton_2.clicked.connect(self.stop)

    @property
    def ui(self):
        return self._ui

    def get_params(self):
        ip = self._ui.lineEdit.text()
        if ip == '':
            QMessageBox.warning(self, 'Предупреждение', 'Вы не ввели IP-адрес!')
        else:
            port = self._ui.lineEdit_2.text()
            try:
                port_num = int(port)
                return ip, port_num
            except ValueError:
                QMessageBox.warning(self, 'Предупреждение', 'Неправильный формат поля "Порт"')
        return '', 0

    def open(self) -> None:
        self._ui.show()

    def start(self) -> None:
        ip, port = self.get_params()
        if ip != '' and port != 0:
            self._server = Server(ip, port, self)
            self._server.start()
            self._ui.pushButton.setEnabled(False)
            self._ui.pushButton_2.setEnabled(True)
            self._ui.label_3.setText('Статус: включен')
            self._ui.label_3.setStyleSheet('color: green')

    def stop(self) -> None:
        self._server.stop()
        self._ui.pushButton.setEnabled(True)
        self._ui.pushButton_2.setEnabled(False)
        self._ui.label_3.setText('Статус: выключен')
        self._ui.label_3.setStyleSheet('color: red')


