from client.gui import ClientWindow
from PyQt5.QtWidgets import QApplication
from sys import exit

if __name__ == '__main__':
    app = QApplication([])
    client_win = ClientWindow()
    client_win.open()
    exit(app.exec())
