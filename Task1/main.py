import json


def task() -> float:
    with open("input.json", "r", encoding="utf-8") as file:
        dct = json.load(file)  # десереализация json файла

    lst1 = [elem_dct["score"] for elem_dct in dct]  # список параметра score
    lst2 = [elem_dct["weight"] for elem_dct in dct]  # список параметра weight
    summ = 0

    for i in range(len(lst1)):
        summ += lst1[i] * lst2[i]  # подсчёт суммы

    return round(summ, 3)


print(task())
