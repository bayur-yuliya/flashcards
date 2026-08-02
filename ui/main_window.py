from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow,
    QPushButton,
    QGridLayout,
    QVBoxLayout,
    QWidget,
    QScrollArea,
    QStackedWidget,
    QLabel,
)

import setup
from ui.topic_window import TopicPage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 100, 600, 600)
        self.setWindowTitle("Flashcards")

        self.setup_ui()

    def setup_ui(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        main_layout.setContentsMargins(20, 20, 20, 20)

        # Главный переключатель страниц
        self.pages = QStackedWidget()

        # Создаём главную страницу
        self.main_page = self.create_main_page()

        # Добавляем её в QStackedWidget
        self.pages.addWidget(self.main_page)

        # Показываем главную страницу
        self.pages.setCurrentWidget(self.main_page)

        main_layout.addWidget(self.pages)

    def create_main_page(self):
        page = QWidget()

        layout = QVBoxLayout(page)

        title = QLabel("Flashcards")

        title.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
            }
        """)

        layout.addWidget(title)

        # ScrollArea
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Контейнер тем
        scroll_content = QWidget()

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

            button.setProperty("button_type", "topic")

            button.clicked.connect(
                lambda checked=False, name=topic: self.topic_clicked(name)
            )

            topics_layout.addWidget(
                button,
                row,
                column,
            )

        scroll_area.setWidget(scroll_content)

        layout.addWidget(scroll_area)

        return page

    def topic_clicked(self, topic):
        # Создаём страницу темы
        topic_page = TopicPage(
            topic_name=topic,
            go_back=self.show_main_page,
        )

        # Добавляем её в QStackedWidget
        self.pages.addWidget(topic_page)

        # Переключаемся на неё
        self.pages.setCurrentWidget(topic_page)

    def show_main_page(self):
        self.pages.setCurrentWidget(self.main_page)
