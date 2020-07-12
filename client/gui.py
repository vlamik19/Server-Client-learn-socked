from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.uic import loadUi


class ClientWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self._ui = loadUi('Client.ui')
        self._client = None
        self._ui.pushButton.clicked.connect(self.start_login)
        self._ui.pushButton_2.clicked.connect(self.stop_login)
        self._ui.pushButton_3.clicked.connect(self.start_connect)
        self._ui.pushButton_4.clicked.connect(self.stop_connect)

    @property
    def ui(self):
        return self._ui

    def open(self) -> None:
        self._ui.show()

    def get_params_login(self):
        login = self._ui.lineEdit.text()
        if login != '':
            QMessageBox.information(self, 'Сообщение', f'Добро пожаловать {login}')
            return login
        else:
            QMessageBox.warning(self, 'Предупреждение', 'Вы не ввели Ваш логин!')
        return ''

    def get_params_connect(self):
        ip = self._ui.lineEdit_2.text()
        if ip == '':
            QMessageBox.warning(self, 'Предупреждение', 'Вы не ввели IP-адрес!')
        else:
            port = self._ui.lineEdit_3.text()
            try:
                port_num = int(port)
                return ip, port_num
            except ValueError:
                QMessageBox.warning(self, 'Предупреждение', 'Неправильный формат поля "PORT"')
        return '', 0

    def start_login(self) -> None:
        login = self.get_params_login()
        if login != '':
            self._ui.pushButton.setEnabled(False)
            self._ui.pushButton_2.setEnabled(True)
            self._ui.lineEdit_2.setEnabled(True)
            self._ui.lineEdit_3.setEnabled(True)
            self._ui.pushButton_3.setEnabled(True)

    def stop_login(self) -> None:
        self._ui.pushButton.setEnabled(True)
        self._ui.pushButton_2.setEnabled(False)
        self._ui.lineEdit_2.setEnabled(False)
        self._ui.lineEdit_3.setEnabled(False)
        self._ui.pushButton_3.setEnabled(False)
        self._ui.pushButton_4.setEnabled(False)
        self._ui.textEdit.setEnabled(False)
        self._ui.pushButton_5.setEnabled(False)
        self._ui.label_4.setText('Статус: Выключен')
        self._ui.label_4.setStyleSheet('color: red')

    def start_connect(self) -> None:
        ip, port = self.get_params_connect()
        if ip != '' and port != 0:
            self._ui.pushButton_3.setEnabled(False)
            self._ui.pushButton_4.setEnabled(True)
            self._ui.textEdit.setEnabled(True)
            self._ui.pushButton_5.setEnabled(True)
            self._ui.label_4.setText('Статус: Включен')
            self._ui.label_4.setStyleSheet('color: green')

    def stop_connect(self) -> None:
        self._ui.pushButton_3.setEnabled(True)
        self._ui.pushButton_4.setEnabled(False)
        self._ui.textEdit.setEnabled(False)
        self._ui.pushButton_5.setEnabled(False)
        self._ui.label_4.setText('Статус: Выключен')
        self._ui.label_4.setStyleSheet('color: red')
