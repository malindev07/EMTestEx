from dataclasses import dataclass, field

from books_repo.book_storage import BookStorage

from settings.commands import Commands
from books_repo.book_actions import ActionBook
from settings.settings import Settings


@dataclass
class RouteBookAction:
    book_storage: BookStorage
    actions_book: ActionBook = field(default=ActionBook)

    # Маршрутизатор для определения действий по введенной команде
    def route_action(self, num_action: Commands):
        self.actions_book = ActionBook(book_storage=self.book_storage)

        try:
            print(f"\nВы выбрали {Settings.action_with_books[num_action]}")

            match num_action:
                case Commands.ADD_BOOK:
                    self.actions_book.add_book()

                case Commands.DELETE_BOOK:
                    pass

                case Commands.FIND_BOOK:
                    pass

                case Commands.SHOW_BOOKS:
                    pass

                case Commands.CHANGE_BOOK_STATUS:
                    pass

        # Если пользователь вводит не существующий номер команды
        except ValueError:
            print(
                f"Команды с номером {num_action} не существует, введите корректный номер\n"
            )
