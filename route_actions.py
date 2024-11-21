from dataclasses import dataclass

from book_model import Book
from crud import ActionBook

from settings import action_with_books


@dataclass
class RouteBookAction:

    # Маршрутизатор для определения действий по введенной команде
    @staticmethod
    def route_action(num_action: str):

        try:
            print(f"\nВы выбрали {action_with_books[num_action]}")
            match num_action:
                case "1":
                    new_book = Book(
                        book_title=input("Введите название книги: "),
                        book_author=input("Введите автора книги: "),
                        book_year=input("Введите год издания книги: "),
                    )
                    print(ActionBook.add_book(book=new_book))

        # Если пользователь вводит не существующий номер команды
        except KeyError:
            print(
                f"Команды с номером {num_action} не существует, введите корректный номер\n"
            )
        #     case '2':
        #     case '3':
        #     case '4':
        #
