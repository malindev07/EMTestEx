import json
from typing import TextIO


# Загружаем данные в бд
def update_db(obj: object, file: TextIO):
    json.dump(obj, file, ensure_ascii=False, indent=4)
