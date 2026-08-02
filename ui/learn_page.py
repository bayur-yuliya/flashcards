from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFrame,
)

import setup


class FlashcardWidget(QFrame):
    clicked = Signal()

    def __init__(self, front, back):
        super().__init__()

        self.front = front
        self.back = back

        # False = первая сторона, True = вторая сторона
        self.is_back_visible = False

        self.setup_ui()
        self.update_card()

    def setup_ui(self):
        self.setMinimumHeight(400)

        self.setStyleSheet(f"""
            QFrame {{
                border: 1px solid #cccccc;
                border-radius: 12px;
                background-color: {setup.LIGHT_COLOR};
            }}
        """)

        layout = QVBoxLayout(self)

        layout.setContentsMargins(
            30,
            30,
            30,
            30,
        )

        self.text_label = QLabel()

        self.text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.text_label.setWordWrap(True)

        self.text_label.setStyleSheet("""
            QLabel {
                border: none;
                background: transparent;
                color: black;
                font-size: 32px;
                font-weight: bold;
            }
        """)

        layout.addWidget(self.text_label)

    def update_card(self):
        if self.is_back_visible:
            self.text_label.setText(self.back)
        else:
            self.text_label.setText(self.front)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:

            # Переворачиваем карточку
            self.is_back_visible = not self.is_back_visible

            # Обновляем текст
            self.update_card()

            # Сообщаем, что карточку нажали
            self.clicked.emit()

        super().mousePressEvent(event)


class LearnPage(QWidget):
    def __init__(self, topic_name, go_back):
        super().__init__()

        self.topic_name = topic_name

        # Функция для возврата назад
        self.go_back = go_back

        self.cards = [
            ("class", "класс"),
            ("object", "объект"),
            ("inheritance", "наследование"),
            ("encapsulation", "инкапсуляция"),
            ("polymorphism", "полиморфизм"),
            ("abstraction", "абстракция"),
            ("method", "метод"),
            ("attribute", "атрибут"),
        ]

        # Индекс текущей карточки
        self.current_card_index = 0

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        title = QLabel(self.topic_name)

        title.setStyleSheet("""
            QLabel {
                font-size: 28px;
                font-weight: bold;
            }
        """)

        main_layout.addWidget(title)

        # Получаем первую карточку
        front, back = self.cards[self.current_card_index]

        # Создаём виджет карточки
        self.card = FlashcardWidget(
            front,
            back,
        )

        # Карточка занимает всё свободное место
        main_layout.addWidget(
            self.card,
            1,
        )

        # Кнопки
        buttons_layout = QHBoxLayout()

        buttons_layout.setSpacing(15)

        self.dont_know_button = QPushButton("Не знаю")
        self.know_button = QPushButton("Знаю")
        back_button = QPushButton("Назад")

        self.dont_know_button.setProperty(
            "button_type",
            "pink_button",
        )

        self.know_button.setProperty(
            "button_type",
            "green_button",
        )

        back_button.setProperty(
            "button_type",
            "back_button",
        )

        buttons_layout.addWidget(self.dont_know_button)

        buttons_layout.addWidget(self.know_button)

        # Раздвигаем кнопку "Назад" вправо
        buttons_layout.addStretch()

        buttons_layout.addWidget(back_button)

        main_layout.addLayout(buttons_layout)

        # События
        self.dont_know_button.clicked.connect(self.dont_know)

        self.know_button.clicked.connect(self.know)

        back_button.clicked.connect(self.go_back)

    def show_next_card(self):
        # Переходим к следующей карточке
        self.current_card_index += 1

        # Если дошли до конца —
        # начинаем сначала
        if self.current_card_index >= len(self.cards):
            self.current_card_index = 0

        # Получаем новую карточку
        front, back = self.cards[self.current_card_index]

        # Обновляем данные существующего виджета
        self.card.front = front
        self.card.back = back

        # Новая карточка всегда начинается
        # с первой стороны
        self.card.is_back_visible = False

        self.card.update_card()

    def dont_know(self):

        self.dont_know_button.clicked.connect(self.show_next_card)

    def know(self):

        self.know_button.clicked.connect(self.show_next_card)
