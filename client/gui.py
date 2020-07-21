from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi
from client.lib import Client


class ClientWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('Client.ui')
        self._client = None
        self._ui.pushButton_3.clicked.connect(self.start_connect)
        self._ui.pushButton_4.clicked.connect(self.stop_connect)
        self._ui.pushButton_5.clicked.connect(self.start_connect)

    @property
    def ui(self):
        return self._ui

    def open(self) -> None:
        self._ui.show()

    def get_params_connect(self):
        login = self._ui.lineEdit.text()
        ip = self._ui.lineEdit_2.text()
        if ip == '':
            QMessageBox.warning(self, 'Предупреждение', 'Вы не ввели IP-адрес!')
        elif login == '':
            QMessageBox.warning(self, 'Предупреждение', 'Вы не ввели логин!')
        else:
            port = self._ui.lineEdit_3.text()
            try:
                port_num = int(port)
                return ip, port_num, login
            except ValueError:
                QMessageBox.warning(self, 'Предупреждение', 'Неправильный формат поля "Порт"')
        return '', 0, ''

    def start_connect(self) -> None:
        ip, port, login = self.get_params_connect()
        if ip != '' and port != 0 and login != '':
            # BUTTONS
            self._ui.pushButton_3.setEnabled(False)
            self._ui.pushButton_4.setEnabled(True)
            self._ui.pushButton_5.setEnabled(True)
            # TEXT_EDIT
            self._ui.textEdit.setEnabled(True)
            # LINE_EDIT
            self._ui.lineEdit_4.setEnabled(True)
            # LABEL
            self._ui.label_4.setText('Статус: Включен')
            self._ui.label_4.setStyleSheet('color: green')

            self._client = Client(ip, port, login, self)
            self._client.start()

    def stop_connect(self) -> None:
        # BUTTONS
        self._ui.pushButton_3.setEnabled(True)
        self._ui.pushButton_4.setEnabled(False)
        self._ui.pushButton_5.setEnabled(False)
        # TEXT_EDIT
        self._ui.textEdit.setEnabled(False)
        # LABEL
        self._ui.label_4.setText('Статус: Выключен')
        self._ui.label_4.setStyleSheet('color: red')
        # LINE_EDIT
        self._ui.lineEdit_4.setEnabled(False)








