from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QLineEdit,
    QScrollArea,
    QFrame,
)


class CardRow(QFrame):
    def __init__(self, front, back):
        super().__init__()

        self.setup_ui(front, back)

    def setup_ui(self, front, back):
        self.setFrameShape(QFrame.NoFrame)

        layout = QHBoxLayout(self)

        self.front_edit = QLineEdit(front)
        self.back_edit = QLineEdit(back)

        self.edit_button = QPushButton("Изменить")
        self.delete_button = QPushButton("Удалить")

        self.edit_button.setProperty(
            "button_type",
            "green_button",
        )

        self.delete_button.setProperty(
            "button_type",
            "pink_button",
        )

        layout.addWidget(self.front_edit)
        layout.addWidget(self.back_edit)
        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)


class EditPage(QWidget):
    def __init__(
        self,
        go_back,
        create_mode=True,
    ):
        super().__init__()

        self.go_back = go_back
        self.create_mode = create_mode

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

        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        title = QLabel("Редактор темы")

        title.setStyleSheet("""
            QLabel{
                font-size:28px;
                font-weight:bold;
            }
        """)

        main_layout.addWidget(title)

        topic_layout = QHBoxLayout()

        self.topic_edit = QLineEdit()

        if self.create_mode:
            self.topic_button = QPushButton("Добавить")
        else:
            self.topic_edit.setText("Python")
            self.topic_button = QPushButton("Изменить")

        self.topic_button.setProperty(
            "button_type",
            "green_button",
        )

        topic_layout.addWidget(self.topic_edit)
        topic_layout.addWidget(self.topic_button)

        main_layout.addLayout(topic_layout)

        card_layout = QHBoxLayout()

        self.front_edit = QLineEdit()
        self.front_edit.setPlaceholderText("Первая сторона")

        self.back_edit = QLineEdit()
        self.back_edit.setPlaceholderText("Вторая сторона")

        self.add_button = QPushButton("Добавить")

        self.add_button.setProperty(
            "button_type",
            "green_button",
        )

        card_layout.addWidget(self.front_edit)
        card_layout.addWidget(self.back_edit)
        card_layout.addWidget(self.add_button)

        main_layout.addLayout(card_layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        container = QWidget()

        self.cards_layout = QVBoxLayout(container)

        self.cards_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        scroll.setWidget(container)

        main_layout.addWidget(scroll)

        bottom_layout = QHBoxLayout()

        bottom_layout.addStretch()

        back_button = QPushButton("Назад")

        back_button.setProperty(
            "button_type",
            "back_button",
        )

        bottom_layout.addWidget(back_button)

        main_layout.addLayout(bottom_layout)

        if not self.create_mode:
            for front, back in self.cards:
                self.add_card_widget(front, back)

        self.add_button.clicked.connect(self.add_card)

        back_button.clicked.connect(self.go_back)

    def add_card(self):
        front = self.front_edit.text().strip()
        back = self.back_edit.text().strip()

        if not front or not back:
            return

        self.add_card_widget(front, back)

        self.front_edit.clear()
        self.back_edit.clear()

    def add_card_widget(self, front, back):
        row = CardRow(front, back)

        row.delete_button.clicked.connect(lambda: self.remove_card(row))

        row.edit_button.clicked.connect(lambda: self.save_card(row))

        self.cards_layout.addWidget(row)

    def remove_card(self, row):
        row.setParent(None)
        row.deleteLater()

    def save_card(self, row):
        print(
            row.front_edit.text(),
            row.back_edit.text(),
        )
