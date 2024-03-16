import csv
"""импортируем библиотеку csv для работы с файлом"""

with open("books.csv", encoding="utf8") as f:
    """откарываем файл"""

    r = list(csv.DictReader(f, delimiter=";"))
    """переводим его в формат списка со словарями"""

    books_rowling = list()
    """создаём список куда будем записывать кники Дж.К. Роулинг"""

    for i in r:
        if "Дж.К. Роулинг" in i["authors"]:
            books_rowling.append({"book_id": i["book_id"], "authors": i["authors"], "original_title": i["original_title"], "ratings_1": i["ratings_1"]})
            """помещаем подходящие книги в список"""

            if float(i["ratings_1"].replace(",", ".")) > 8:
                print(f"{i["authors"]} - {i["original_title"]}\t{i["ratings_1"]}")
            """и выводим книги Дж.К. Роулинг с рейтингом выше 8"""


with open("books_rowling.csv", "w", encoding="utf8") as nf:
    """создаём новый файл"""

    w = csv.DictWriter(nf, delimiter=";", quotechar='"', fieldnames=["book_id", "authors", "original_title", "ratings_1"])
    w.writeheader()
    w.writerows(books_rowling)
    """записываем книги Дж.К. Роулинг в файл"""