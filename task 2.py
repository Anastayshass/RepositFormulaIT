# TODO Напишите функцию find_common_participants
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

def find_common_participants(participants_first_group, participants_second_group, r=','):
    list = []  # Новый список общих участников
    list1 = participants_first_group.split(r)  # Разбиваем строку по указанному разделителю
    list2 = participants_second_group.split(r)  # Разбиваем строку по указанному разделителю
    for i in list2:  # Создаем цикл для сравнения двух списков участников
        for g in list1:
            if i == g:
                list.append(i)

    list = sorted(list)
    return list

# TODO Провеьте работу функции с разделителем отличным от запятой
n = find_common_participants(participants_first_group, participants_second_group, r='|')
print(n)
