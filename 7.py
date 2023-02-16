# вводим число n с клавиатуры
n = int(input())

# так как у всех чисел с 10 по 19 включительно одинаковое слово "коров",
# а также эти числа исключения от следующих правил (на 1, 2, 3, 4), то сразу прописываем условие
if n // 10 == 1:
    print(str(n) + ' korov')

# ко всем числам, оканчивающимся на 1 добавляется слово "корова", например "71 корова"
elif n % 10 == 1:
    print(str(n) + ' korova')

# ко всем числам, оканчивающимся на 2, 3, 4 добавляется слово "коровы", например "54 коровы "
elif (n % 10 == 2) or (n % 10 == 3) or (n % 10 == 4):
    print(str(n) + ' korovy')

# во всех остальных случаях добавляем слово "коров"
else:
    print(str(n) + ' korov')
