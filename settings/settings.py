from dataclasses import dataclass, field
from typing import ClassVar


@dataclass
class Settings:

    action_with_books: ClassVar[dict[str, str]] = {
        "1": "Добавить книгу",
        "2": "Удалить книгу",
        "3": "Поиск книги",
        "4": "Изменение статуса книги",
    }

    @classmethod
    def display_actions(cls):
        for num, action in cls.action_with_books.items():
            print(f"{num} - {action}")
