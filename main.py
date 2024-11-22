from books_repo.book_storage import BookStorage
from settings.commands import Commands

from router.route_actions import RouteBookAction
from settings.settings import Settings

if __name__ == "__main__":
    book_storage = BookStorage()
    book_storage.get_storage()
    router = RouteBookAction(book_storage=book_storage)

    while True:
        print("Выберите номер команды:")

        Settings.display_actions()

        try:
            action_num = Commands(input("Введите номер команды: "))
            router.route_action(action_num)
        except ValueError:
            print(f"Такой команды не существует, введите корректный номер\n")
