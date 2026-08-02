from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QScrollArea,
    QTextEdit,
)

import setup


class TopicPage(QWidget):
    def __init__(self, topic_name, go_back, learn_topic):
        super().__init__()

        self.topic_name = topic_name
        self.go_back = go_back
        self.learn_topic_callback = learn_topic
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

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

        learn_button.setProperty(
            "button_type",
            "green_button",
        )

        edit_button.setProperty(
            "button_type",
            "pink_button",
        )

        back_button.setProperty(
            "button_type",
            "back_button",
        )

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

        cards_text = "\n".join(f"{front} - {back}" for front, back in cards)

        cards_text_edit = QTextEdit()

        cards_text_edit.setPlainText(cards_text)

        # Только просмотр, редактировать нельзя
        cards_text_edit.setReadOnly(True)

        # Можно выделять мышкой и клавиатурой
        cards_text_edit.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse
            | Qt.TextInteractionFlag.TextSelectableByKeyboard
        )

        cards_text_edit.setStyleSheet(f"""
            QTextEdit {{
                border: 1px solid #cccccc;
                border-radius: 8px;
                background-color: {setup.LIGHT_COLOR};
                color: black;
                font-size: 16px;
                padding: 10px;
            }}
        """)

        scroll_area.setWidget(cards_text_edit)

        main_layout.addWidget(scroll_area)

        learn_button.clicked.connect(self.learn_topic)
        edit_button.clicked.connect(self.edit_topic)
        back_button.clicked.connect(self.go_back)

    def learn_topic(self):
        self.learn_topic_callback(self.topic_name)

    def edit_topic(self):
        print(f"Editing topic: {self.topic_name}")
