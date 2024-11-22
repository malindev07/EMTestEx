import json
from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class BookStorage:
    storage: dict[str, dict[str, str]] = field(default_factory=dict)
    db_path: Path = Path(Path.cwd(), Path("db"), Path("books_db.json"))

    def get_storage(self):
        try:
            with self.db_path.open("r", encoding="utf-8") as fp:
                books_data = json.load(fp=fp)
                self.storage = books_data

        except json.decoder.JSONDecodeError:
            pass

    def set_storage(self) -> bool:
        try:
            with self.db_path.open("w", encoding="utf-8") as fp:
                json.dump(self.storage, fp=fp, indent=4, ensure_ascii=False)
                return True
        except FileNotFoundError:
            return False