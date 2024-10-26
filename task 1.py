money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months = 0 # Кол-во месяцев без долгов
remains = money_capital + salary - spend # Остаток за первый месяц

if remains >= 0: # Проверка остатка за первый месяц
    months += 1

while remains >= 0: # Проверка остатка за следующие месяцы
    spend = spend + (spend * increase)
    remains = salary + remains - spend
    if remains >= 0:
        months += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
