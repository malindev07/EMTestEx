from last_id import get_last_id
from route_actions import RouteBookAction
from settings import action_with_books, last_id

if __name__ == "__main__":
    last_id["id"] = get_last_id()

    while True:
        print("Выберите номер команды:")
        for num, action in action_with_books.items():
            print(f"{num} - {action}")
        action_num = input("Введите номер команды: ")
        RouteBookAction.route_action(action_num)
