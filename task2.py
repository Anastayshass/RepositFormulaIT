# TODO Найдите количество книг, которое можно разместить на дискете
v = float(1.44) * int(2 ** 20)
otvet = v / float(100 * 50 * 25 * 4)
print("Количество книг, помещающихся на дискету:", round(otvet))
