import json


def get_last_id() -> int:
    with open("books_db.json", "r", encoding="utf-8") as f:
        # Пробуем узнать последний добавленный id
        try:
            books = json.loads(f.read())
            return int(list(books)[-1])

        # Если файл пустой, то возвращаем id = 0
        except ValueError:
            return 1
