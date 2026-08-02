import sys
from PySide6.QtWidgets import QApplication

from ui.main_window import MainWindow
from utils.styles import load_stylesheet


def main():
    app = QApplication(sys.argv)

    app.setStyleSheet(load_stylesheet("buttons.qss"))

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
