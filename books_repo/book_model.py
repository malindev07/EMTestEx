from dataclasses import dataclass, field, asdict
from uuid import uuid4
from enum import StrEnum


class BookStatus(StrEnum):
    AVAILIBALE = "в наличии"
    NOT_AVAILIBALE = "выдана"


@dataclass
class Book:

    book_title: str
    book_author: str
    book_year: str
    book_status: BookStatus = field(default=BookStatus.AVAILIBALE)
    book_id: str = field(default_factory=lambda: str(uuid4()))
