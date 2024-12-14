class Cards: # Карточка товара на маркетплейсе
    def __init__(self, art: int, costs: (int, float), description: str):
        if not isinstance(art, int):
            raise TypeError("Артикул должен быть типа int")
        if len(str(art)) != 9:
            raise ValueError("Артикул должен состоять из 9 цифр")
        self.art = art # Артикул

        if not isinstance(costs, (int, float)):
            raise TypeError("Стоимость должна быть типа int или float")
        if costs <= 0:
            raise ValueError("Стоимость должна быть положительным числом")
        self.costs = costs # Стоимость

        if not isinstance(description, str):
            raise TypeError("Описание должно быть типа str")
        self.description = description # Описание

        self.favourites = False  # "Избранное"

    def art_favourites(self):
        if self.favourites == False:
            self.favourites = True
        else:
            self.favourites = False

    def buy(self):
        ...

if __name__ == "__main__":
    card_WB = Cards(120172120, 650, "Моносерьга каффа серебро 925 серебряная ювелирная")
    card_WB.art_favourites()
    print(card_WB.favourites)
    card_WB.art_favourites()
    print(card_WB.favourites)
