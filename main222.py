import random
from faker import Faker
import json
from typing import List, Dict
from conf import MODEL

fake = Faker('ru_RU')


def generate_book(pk: int = 1) -> Dict:

    book = {
        "model": MODEL,
        "pk": pk,
        "fields": {
            "title": random.choice(open("books.txt", "r", encoding='utf-8').read().splitlines()),
            "year": random.randint(1900, 2022),
            "pages": random.randint(50, 1000),
            "isbn13": fake.isbn13(),
            "rating": random.randint(1, 5),
            "price": round(random.uniform(10, 10000), 2),
            "author": [fake.name() for _ in range(random.randint(1, 3))]
        }
    }

    yield book
    pk += 1


def main():
    gen = generate_book(50)
    # book = (generate_book(pk) for pk in range(1, 101))
    for i in range(6):
        books = next(gen)
        print(books)
    # list1 = []
    # for i in range(5):
    #    books = next(gen)

    with open("books.json", "w") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


if __name__ == '__main__':
    main()
