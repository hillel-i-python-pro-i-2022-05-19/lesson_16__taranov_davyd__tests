import hashlib
from typing import TypeAlias, TypedDict, Any


class Item(TypedDict):
    name: str
    age: str
    id: str


T_DB: TypeAlias = list[dict]
T_INDEX: TypeAlias = list[dict[Any, Item]]
T_INDEX__PYTHON: TypeAlias = dict[Any, Item]


def get_data(my_db: T_DB) -> Item:
    for item in my_db:
        if item["id"] == 2:
            return item
        raise KeyError


def creat_index(my_db: T_DB, field_name: str) -> T_INDEX:
    return sorted(({"key": item[field_name], "value": item} for item in my_db), key=lambda x: x["key"])


def creat_index__python(my_db: T_DB, field_name: str) -> T_INDEX__PYTHON:
    return {item[field_name]: item for item in my_db}


def main():
    my_db: T_DB = [
        {
            "name": "Aaa",
            "age": 22,
            "id": 1,
        },
        {
            "name": "Bbb",
            "age": 32,
            "id": 2,
        },
        {
            "name": "Cvv",
            "age": 54,
            "id": 3,
        },
    ]

    index__by__id = creat_index(my_db=my_db, field_name="id")  # noqa: E731
    index__by__name = creat_index(my_db=my_db, field_name="name")  # noqa: E731

    my_db[1]["age"] = 40

    index__by__id_python = creat_index__python(my_db=my_db, field_name="id")  # noqa: E731
    index__by__name_python = creat_index__python(my_db=my_db, field_name="name")  # noqa: E731

    word = "hello"
    word_hash = hash(word)  # noqa: E731

    word_hash2 = hashlib.sha3_512(word.encode())
    a = word_hash2.hexdigest()  # noqa: E731

    salt = "bla foo bar"
    word_hash2.update(salt.encode())
    b = word_hash2.hexdigest()  # noqa: E731

    print("hi")


if __name__ == "__main__":
    main()
