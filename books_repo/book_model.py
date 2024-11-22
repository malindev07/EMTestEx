from dataclasses import dataclass, field, asdict
from uuid import uuid4
from enum import StrEnum


# @dataclass
# class BookId:
#     book_id: str = ""
#
#     @staticmethod
#     def set_book_id():
#         book_id: str = str(last_id["id"])
#         last_id["id"] += 1
#         return book_id


class BookStatus(StrEnum):
    AVAILIBALE = "в наличии"
    NOT_AVAILIBALE = "выдана"


@dataclass
class Book:

    book_title: str
    book_author: str
    book_year: str
    book_status: BookStatus = field(default=BookStatus.AVAILIBALE)
    # book_status: Literal["в наличии", "выдана"] = field(default="в наличии")
    book_id: str = field(default_factory=lambda: str(uuid4()))
