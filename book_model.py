import enum

from black.cache import dataclass

from settings import last_id


@dataclass
class BookId:
    book_id: str = ""

    @staticmethod
    def set_book_id():
        book_id: str = str(last_id["id"])
        last_id["id"] += 1
        return book_id


class BookStatus(enum.Enum):
    available_book = "в наличии"
    not_available_book = "выдана"


class Book:
    # book_id: str = ''

    def __init__(self, book_title: str, book_author: str, book_year: str):
        self.book_id = BookId.set_book_id()
        self.book_title = book_title
        self.book_author = book_author
        self.book_year = book_year
        self.book_status = BookStatus.available_book.value


# a = Book(book_title="123", book_author="123", book_year="123")
# b = Book(book_title="123", book_author="123", book_year="123")
#
# print(json.dumps(a, default=class_to_dict, ensure_ascii=False, indent=4))

# with open("books_db.json", "w", encoding="utf-8") as outfile:
#     json.dump(a, outfile, default=class_to_dict, ensure_ascii=False, indent=4)
