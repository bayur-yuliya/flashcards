from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setWindowTitle("Flashcards")
        self.setGeometry(100, 100, 800, 600)

        self.create_menu()
        self.statusBar().showMessage("Message")

    def create_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Menu")

        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
