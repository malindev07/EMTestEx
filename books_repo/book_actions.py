from dataclasses import dataclass, asdict

from books_repo.book_storage import BookStorage
from books_repo.book_model import Book, BookStatus


@dataclass
class ActionBook:
    book_storage: BookStorage

    # Добавление книги
    def add_book(self) -> None:
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

        except (KeyError, ValueError):
            print("Ошибка! Автор и название не могут быть пустыми!")

    # Удаление книги по id
    def delete_book(self) -> None:
        book_id: str = input("Введите id книги: ")

        try:

            self.book_storage.storage.pop(book_id)

            print(f"Книга с id {book_id} удалена!")
            self.book_storage.set_storage()

        except KeyError:
            print(f"Книга с id {book_id} не найдена!")

    # Поиск книги по автору, названию или году выпуска
    def find_book(self) -> None:
        book_for_find: str = input("Введите название, автора или год книги: ")

        try:

            coincidence: bool = False
            print(f"Книга по запросу {book_for_find}")

            for book in self.book_storage.storage.values():
                for item in book:
                    if book[item] == book_for_find:
                        print(
                            f"Название книги - {book['book_title']}, id книги - {book['book_id']} "
                        )

                        coincidence = True
                        break

            if not coincidence:
                print("Книга не найдена\n")

        except ValueError:
            print("Недопустимое значение для полей название, автор, год.")

    # Отображение всех книг
    def show_books(self):
        for book in self.book_storage.storage.values():
            print(
                f"id книги: {book['book_id']}, название книги: "
                f"{book['book_title']}, автор книги: {book['book_author']}, год издания: {book['book_year']}, статус книги: "
                f"{book['book_status']}"
            )
        print("\n")

    # Изменение статуса книги
    def change_book_status(self):
        book_id: str = input("Введите id книги: ")

        try:
            if (
                self.book_storage.storage[book_id]["book_status"]
                == BookStatus.AVAILIBALE
            ):
                self.book_storage.storage[book_id].update(
                    book_status=BookStatus.NOT_AVAILIBALE
                )
            else:
                self.book_storage.storage[book_id].update(
                    book_status=BookStatus.AVAILIBALE
                )

            self.book_storage.set_storage()
            print(
                f"Статус книги с id {book_id} изменен! Текущий статус - {self.book_storage.storage[book_id]['book_status']}\n"
            )

        except KeyError:
            print(f"Книга c id {book_id} не найдена. \n")
