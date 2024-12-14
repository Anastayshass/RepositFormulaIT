class Basket: # Корзина на маркетплейсе
    def __init__(self, purchase: (int, float), address: str, count: int):
        if not isinstance(purchase, (int, float)):
            raise TypeError("Сумма к оформлению должна быть типа int или float")
        if purchase < 0:
            raise ValueError("Сумма к оформлению должна быть положительным числом (или 0)")
        self.purchase = purchase # "К оформлению"
        if self.purchase == 0:
            print()

        if not isinstance(address, str):
            raise TypeError("Пункт выдачи должен быть типа str")
        self.address = address # Пункт выдачи

        if not isinstance(count, int):
            raise TypeError("Количество товаров должно быть типа int")
        if count < 0:
            raise ValueError("Количество товаров должно быть положительным числом (или 0)")
        self.count = count # "Количество товаров"
        if self.count == 0:
            print()

    def buy(self): # "Купить"
        ...

    def delete(self, delete: int): # "К удалению"
        if not isinstance(delete, int):
            raise TypeError("Сумма к удалению должна быть типа int")
        if delete < 0:
            raise ValueError("Сумма к удалению должна быть положительным числом (или 0)")
        self.count = self.count - delete
        ...

if __name__ == "__main__":
    basket_WB = Basket(60210, "г. Королёв, улица Космонавта Стрекалова, 34", 75)
    basket_WB.delete(3)
    print(basket_WB.count)
