import json
from dataclasses import dataclass
from idlelib.iomenu import encoding

from book_model import Book
from convert_class_to_dict import class_to_dict
from update_db import update_db


# Реализация CRUD


@dataclass
class ActionBook:

    # Добавление книги в базу, если такой книги нет в бд, в противном случае сообщение о наличии такой книги.
    @classmethod
    def add_book(cls, book: Book) -> str:
        with open("books_db.json", "r+", encoding="utf-8") as f:
            try:
                books: dict = json.loads(f.read())

                books.update(class_to_dict(book))

                f.seek(0)

                update_db(obj=books, file=f)

            except ValueError:
                update_db(obj=class_to_dict(book), file=f)

        return f"Книга {book.book_title} добавлена!\n"
