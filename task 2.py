salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0 # Подушка безопасности

money_capital = salary - spend # Долг за первый месяц
month = months - 1 # Прошёл 1 месяц

while month > 0: # Процесс расчёта долга
    month -= 1
    spend = spend + (spend * increase) # Траты за каждый следующий месяц
    money_capital = money_capital + salary - spend # Долг за каждый следующий месяц

money_capital /= -1 # Перевод долга в подушку безопасности

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(money_capital))
