import csv
"""импортируем библиотеку csv для работы с файлом"""

with open("books.csv", encoding="utf8") as f:
    """откарываем файл"""

    r = list(csv.DictReader(f, delimiter=";"))
    """переводим его в формат списка со словарями"""

    for i in r:
        ratBook = float(i["ratings_1"].replace(",", "."))
        """переводим рейтинг в формат float"""

        if ratBook < 5:
            i["grade"] = "не рекомендовать"

        elif 5 <= ratBook < 8:
            i["grade"] = "рекомендовать после"

        else:
            i["grade"] = "рекомендовать в первую очередь"

    """перебираем все книги и добавляем нужную оценку"""


with open("books_grade.csv", "w", encoding="utf8") as nf:
    """создаём новый файл"""

    w = csv.DictWriter(nf, delimiter=";", quotechar='"', fieldnames=["book_id", "isbn", "authors", "original_publication_year", "original_title", "ratings_1", "grade"])
    w.writeheader()
    w.writerows(r)
    """записываем туда книги с новой оценкой"""