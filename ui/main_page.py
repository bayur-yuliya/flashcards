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

from ui.edit_page import EditPage
from ui.topic_page import TopicPage
from ui.learn_page import LearnPage


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 100, 600, 600)
        self.setWindowTitle("Flashcards")

        # Хранение текущей страницы
        self.current_topic_page = None
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Главный переключатель страниц
        self.pages = QStackedWidget()

        self.main_page = self.create_main_page()
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
            learn_topic=self.show_learn_page,
            edit_topic=self.show_edit_page,
        )

        self.current_page = topic_page

        # Добавляем её в QStackedWidget
        self.pages.addWidget(topic_page)

        # Переключаемся на неё
        self.pages.setCurrentWidget(topic_page)

    def show_learn_page(self, topic):
        learn_page = LearnPage(
            topic_name=topic,
            go_back=self.show_topic_page,
        )

        self.pages.addWidget(learn_page)
        self.pages.setCurrentWidget(learn_page)

    def show_topic_page(self):
        if self.current_page is not None:
            self.pages.setCurrentWidget(self.current_page)

    def show_main_page(self):
        self.pages.setCurrentWidget(self.main_page)

    def show_edit_page(self, topic):
        edit_page = EditPage(
            go_back=self.show_topic_page,
            create_mode=False,
        )

        self.pages.addWidget(edit_page)
        self.pages.setCurrentWidget(edit_page)
