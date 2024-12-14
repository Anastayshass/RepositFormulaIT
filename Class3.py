import doctest

class PowerBank: # Объект павербанк
    def __init__(self, power_now: float, battery_capacity: float, status: bool):
        if not isinstance(power_now, (int, float)):
            raise TypeError("Заряд PB должен быть типа int или float")
        if power_now < 0:
            raise ValueError("Заряд PB должен быть положительным числом (или 0)")
        if power_now > 100:
            raise ValueError("Заряд должен быть не более 100%")
        self.power_now = power_now
        if power_now <= 3:
            print(f"У вас осталось {power_now}%")
        else:
            print(f"{power_now}%")
        """
        Пример:
        >>> my_PB = PowerBank(99, 5000, False)  # инициализация экземпляра класса
        """

        if not isinstance(battery_capacity, (int, float)):
            raise TypeError("Мощность PB должна быть типа int или float")
        if battery_capacity <= 0:
            raise ValueError("Мощность PB должна быть положительным числом")
        self.battery_capacity = battery_capacity

        if not isinstance(status, bool):
            raise TypeError("Статус использования должен быть типа True или False")
        self.status = status # Статус PB (используется ли пользователем в данный момент)
        if status:
            print("Используется")
        else:
            print("Не используется")

    def charge_PB(self, power: float) -> None: # Зарядка павербанка
        if not isinstance(power, (int, float)):
            raise TypeError("Заряд должен быть типа int или float")
        if power < 0:
            raise ValueError("Заряд должен быть положительным числом (или 0)")
        if power > 100:
            raise ValueError("Заряд должен быть не более 100%")
        ...
        """
        Пример:
        >>> my_PB = PowerBank(99, 5000, False)
        >>> my_PB.charge_PB(100)
        """

    def temperature(self) -> None:  # Температура павербанка
        if self.status == True and self.power_now < 52:
            print("PowerBank перегрелся")
        else:
            print("Температура PowerBank в норме")
        ...
        """
        Пример:
        >>> my_PB = PowerBank(99, 5000, False)
        >>> my_PB.temperature()
        """

if __name__ == "__main__":
    doctest.testmod()