from server.gui import ServerWindow
from PyQt5.QtWidgets import QApplication
from sys import exit

if __name__ == '__main__':
    app = QApplication([])
    server_win = ServerWindow()
    server_win.open()
    exit(app.exec())
