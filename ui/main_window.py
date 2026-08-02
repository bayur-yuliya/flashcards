from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QWidget,
    QScrollArea,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(300, 200, 600, 600)
        self.setWindowTitle("Flashcards")

        self.setUpUI()
        self.statusBar().showMessage("Message")

    def setUpUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)

        # Контейнер для содержимого ScrollArea
        scroll_content = QWidget()

        # Сетка с темами
        topics_layout = QGridLayout(scroll_content)
        topics_layout.setContentsMargins(0, 0, 0, 0)
        topics_layout.setSpacing(15)
        topics_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        topics = [
            "Python",
            "Django",
            "English",
            "SQL",
            "PostgreSQL",
            "Git",
            "Docker",
            "Algorithms",
        ]

        columns = 2

        for index, topic in enumerate(topics):
            row = index // columns
            column = index % columns

            button = QPushButton(topic)
            button.setMinimumHeight(100)

            button.setStyleSheet("""
                QPushButton {
                    font-size: 18px;
                    font-weight: bold;
                    border: 1px solid #cccccc;
                    border-radius: 10px;
                    background-color: #f5f5f5;
                    color: black;
                }

                QPushButton:hover {
                    background-color: #e8e8e8;
                }

                QPushButton:pressed {
                    background-color: #dcdcdc;
                }
            """)

            button.clicked.connect(
                lambda checked=False, name=topic: self.topic_clicked(name)
            )

            topics_layout.addWidget(button, row, column)

        # ScrollArea
        scroll_area = QScrollArea()

        scroll_area.setWidget(scroll_content)
        scroll_area.setWidgetResizable(True)

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # Вот сюда добавляем только ScrollArea
        main_layout.addWidget(scroll_area)

    def topic_clicked(self, topic):
        print(f"Selected topic: {topic}")
