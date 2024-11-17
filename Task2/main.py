# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, "r", encoding="utf-8") as file_input:
        reader = csv.DictReader(file_input)
        lst = []  # Список для словарей

        for row in reader: #Добавление в список
            lst.append(row)

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, "w", encoding="utf-8") as file_output:
        json.dump(lst, file_output, indent=4)  #сериализация



if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
