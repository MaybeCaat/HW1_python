# вводим число n с клавиатуры
n = int(input())

# заполняем изначально по цене, сколько влезет
b60 = n // 60
b10 = (n % 60) // 10
b1 = n % 10

# однако есть 2 условия, когда разом будет выгоднее:
# 9 билетов по одному НЕ выгоднее разом 10 (8 по одному - выгоднее, чем разом 10)
# 40 билетов НЕ выгоднее разом 60 (30 по 10 - выгоднее, чем разом 60)

# немного исправляем количество по этим условиям
# если стоимость оставшихся по 1 билету (15 рублей) больше, чем стоимость 10-ти разом (125 рублей),
# то прибавляем один по 10 разом и убираем все билеты по 1
# прибавляем именно 1, так как изначально по заполнению не могло оказаться больше 10
if b1 * 15 > 125:
    b1 = 0
    b10 += 1

# если стоимость оставшихся по 1 билету (15 рублей) и оставшихся по 10 билетов (125 рублей) больше,
# чем стоимость 60-ти разом (440 рублей), то прибавляем один по 60 разом и убираем все билеты по 1 и по 10
# прибавляем именно 1, так как изначально по заполнению не могло оказаться больше 60
if b1 * 15 + b10 * 125 > 440:
    b10 = 0
    b1 = 0
    b60 += 1

# выводим все 3 значения
print(str(b1), str(b10), str(b60))
