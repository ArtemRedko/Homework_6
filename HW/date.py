from datetime import datetime
from sys import argv

__all__ = ['check_year', 'date_validator']

def check_leap_year(date: str) -> bool:   # проверка года на вискосность
    CHECK_NORMAL_1 = 4
    CHECK_NORMAL_2 = 100
    CHECK_NORMAL_3 = 400
    YEARS = range(1, 10000)
    year = int(date.split(".")[-1])
    if year in YEARS and year % CHECK_NORMAL_1 == 0 and year % CHECK_NORMAL_2 != 0 or year % CHECK_NORMAL_3 == 0:
        return True
    return False


def check_year(year: str) -> bool:       # проверка даты на формат
    try:
        _ = datetime.strptime(year, "%d.%m.%Y").date()
        return True
    except:
        return False


def date_conclusion(date_for_check: str) -> str:               # вывод результата
    if check_year(date_for_check):
        return 'Високосный' if check_leap_year(date_for_check) else 'Не является високосным'
    else:
        return f'Дата заполнена некорректно'


if __name__ == "__main__":            # считывание с командной строки
    if len(argv) == 2:
        _, date = argv
        print(date_conclusion(date))
    else:
        print("Дата для проверки не указана!")