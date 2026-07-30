from PySide6.QtWidgets import QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(200, 100, 500, 400)
        self.setWindowTitle("Flashcards")

        self.setUpMenu()
        self.setUpCounter()
        self.statusBar().showMessage("Message")

    def setUpMenu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Menu")

        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)

    def setUpCounter(self):
        self.label = QLabel("Counter", self)
        self.label.move(100, 100)
        self.label_counter = QLabel(str(self.count), self)
        self.label_counter.move(100, 150)
        button = QPushButton("Increase", self)
        button.move(100, 200)
        button.clicked.connect(self.increaseCounter)

    def increaseCounter(self):
        self.count += 1
        self.label_counter.setText(str(self.count))
