import json
from dataclasses import dataclass, asdict

from books_repo.book_storage import BookStorage
from books_repo.book_model import Book


@dataclass
class ActionBook:
    book_storage: BookStorage

    # Добавление книги в базу
    def add_book(self) -> Book | bool:
        new_book = Book(
            book_title=input("Введите название книги: "),
            book_author=input("Введите автора книги: "),
            book_year=input("Введите год издания книги: "),
        )
        try:

            if new_book.book_title == "" or new_book.book_author == "":
                raise ValueError

            self.book_storage.storage[new_book.book_id] = asdict(new_book)
            self.book_storage.set_storage()
            print("Книга " + new_book.book_title + " добавлена!\n")
            return new_book

        except (KeyError, ValueError):
            print("Ошибка! Автор и название не могут быть пустыми!")
            return False

        # # path
        # with open("db/books_db.json", "r+", encoding="utf-8") as f:
        #     try:
        #         books: dict = json.loads(f.read())
        #
        #         books.update(class_to_dict(book))
        #
        #         f.seek(0)
        #
        #         update_db(obj=books, file=f)
        #         return True
        #     except ValueError:
        #         update_db(obj=class_to_dict(book), file=f)

        # return f"Книга {book.book_title} добавлена!\n"

    @classmethod
    def delete_book(cls, book_id: str) -> str:
        with open("../db/books_db.json", "r+", encoding="utf-8") as f:
            try:
                books: dict = json.loads(f.read())

                books.pop(book_id)

                f.seek(0)

                update_db(obj=books, file=f)

                return f"Книга с id {book_id} {books[book_id]['book_title']} удалена."
            except KeyError:
                print("Key")
