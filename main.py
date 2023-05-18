import random
from faker import Faker
import json
from typing import List, Dict
from conf import MODEL

fake = Faker('ru_RU')


def generate_title() -> str:
    """ Генерация случайного названия книги из файла books.txt."""
    with open("books.txt", "r", encoding='utf-8') as file:
        book_titles = file.read().splitlines()
    return random.choice(book_titles)


def generate_year() -> int:
    """ Генерация случайного года из диапазона 1900-2022."""
    return random.randint(1900, 2022)


def generate_pages() -> int:
    """ Генерация случайного количества страниц из диапазона 50-1000."""
    return random.randint(50, 1000)


def generate_isbn() -> str:
    """ Генерация случайного номера ISBN-13 с помощью модуля Faker."""
    return fake.isbn13()


def generate_rating() -> float:
    """ Генерация случайного рейтинга книги от 0 до 5."""
    return round(random.uniform(0, 5), 1)


def generate_price() -> float:
    """ Генерация случайной цены книги от 10 до 10000."""
    return round(random.uniform(10, 10000), 2)


def generate_author() -> List[str]:
    """ Генерация случайных имен и фамилий авторов с помощью модуля Faker."""
    return [fake.name() for _ in range(random.randint(1, 3))]


def generate_book(pk: int = 1) -> Dict:
    """ Генерация случайной книги. :param pk: Начальное значение счётчика для поля `pk`.:return: Словарь, описывающий одну книгу."""
    book = {
        "model": MODEL,
        "pk": pk,
        "fields": {
            "title": generate_title(),
            "year": generate_year(),
            "pages": generate_pages(),
            "isbn13": generate_isbn(),
            "rating": generate_rating(),
            "price": generate_price(),
            "author": generate_author()
        }
    }
    return book


def main():
    """ Функция генерирует 100 книг с помощью функции generate_book и записывает их в файл books.json."""
books = [generate_book(pk=pk) for pk in range(1, 101)]
with open("books.json", "w") as file:
    json.dump(books, file, ensure_ascii=False, indent=4)

# def generate_books():
""" Функция генератор, сдесь с помошью yield мы можем создавать объекты по мере необходимости. Объекты можем получать путем
 итераций при обращении к ней."""
#    for pk in range(1, 101):
#        yield generate_book(pk=pk)


if __name__ == '__main__':
 main()

#    """ Функции генератор generate_books записывает 100 книг в файл books.json."""
#    with open("books.json", "w") as file:
#        for book in generate_books():
#            list1 = []
#            json.dump(book, file, ensure_ascii=False, indent=2)
#            list1.append(book)
