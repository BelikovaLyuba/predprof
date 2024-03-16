import csv
"""импортируем библиотеку csv для работы с файлом"""

with open("books.csv", encoding="utf8") as f:
    """откарываем файл"""
    r = list(csv.DictReader(f, delimiter=";"))
    """переводим его в формат списка со словарями"""

    for i in range(len(r)):
        j = i
        while r[j]["ratings_1"].replace(",", ".") < r[j - 1]["ratings_1"].replace(",", ".") and j - 1 >= 0:
            r[j], r[j - 1] = r[j - 1], r[j]
            j -= 1
    """сортируем список по вознастанию рейтинга"""

    for i in range(3):
        print(f"{r[i]["original_title"]} - {r[i]["authors"]} - {r[i]["ratings_1"]}")
    """выводим 3 книги с самыми низкими рейтингами"""
