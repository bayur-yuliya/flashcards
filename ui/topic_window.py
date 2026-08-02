from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QScrollArea,
    QFrame,
)


class TopicPage(QWidget):
    def __init__(self, topic_name, go_back):
        super().__init__()

        self.topic_name = topic_name
        self.go_back = go_back

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)

        # Название темы
        title = QLabel(self.topic_name)

        title.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
            }
        """)

        main_layout.addWidget(title)

        # Кнопки
        buttons_layout = QHBoxLayout()

        learn_button = QPushButton("Изучить тему")
        edit_button = QPushButton("Изменить")
        back_button = QPushButton("Назад")

        buttons_layout.addWidget(learn_button)
        buttons_layout.addWidget(edit_button)

        # Кнопка назад справа
        buttons_layout.addStretch()
        buttons_layout.addWidget(back_button)

        main_layout.addLayout(buttons_layout)

        # Область карточек
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Контейнер карточек
        cards_container = QWidget()

        cards_layout = QVBoxLayout(cards_container)

        cards_layout.setContentsMargins(0, 0, 0, 0)
        cards_layout.setSpacing(10)

        # Пока карточки захардкожены
        cards = [
            ("class", "класс"),
            ("object", "объект"),
            ("inheritance", "наследование"),
            ("encapsulation", "инкапсуляция"),
            ("polymorphism", "полиморфизм"),
            ("abstraction", "абстракция"),
            ("method", "метод"),
            ("attribute", "атрибут"),
        ]

        for front, back in cards:
            card = self.create_card(front, back)
            cards_layout.addWidget(card)

        # Чтобы карточки не растягивались на всю высоту
        cards_layout.addStretch()

        scroll_area.setWidget(cards_container)

        main_layout.addWidget(scroll_area)

        # События
        learn_button.clicked.connect(self.learn_topic)
        edit_button.clicked.connect(self.edit_topic)
        back_button.clicked.connect(self.go_back)

    def create_card(self, front, back):
        card = QFrame()

        card.setFrameShape(QFrame.Shape.StyledPanel)

        card.setStyleSheet("""
            QFrame {
                border: 1px solid #cccccc;
                border-radius: 8px;
                background-color: #f5f5f5;
            }
        """)

        layout = QHBoxLayout(card)

        front_label = QLabel(front)
        back_label = QLabel(back)

        front_label.setStyleSheet("""
            QLabel {
                border: none;
                font-size: 16px;
                font-weight: bold;
                color: black;
            }
        """)

        back_label.setStyleSheet("""
            QLabel {
                border: none;
                font-size: 16px;
                color: black;
            }
        """)

        layout.addWidget(front_label)
        layout.addWidget(back_label)

        return card

    def learn_topic(self):
        print(f"Learning topic: {self.topic_name}")

    def edit_topic(self):
        print(f"Editing topic: {self.topic_name}")
