# вводим число x с клавиатуры
x = int(input())

# делим число на десятки tens и единицы units
tens = x // 10
units = x % 10

# 100 - отдельный случай, только С
# отдельно делаем ещё условия на 4 и 9, так как они записываются по-другому,
# а также числа от 5 включительно и меньше 5 записываются по-разному
if tens == 10:
    result = "C"
elif tens == 9:
    result = "XC"
elif tens == 4:
    result = "XL"
elif tens >= 5:
    result = "L" + (tens - 5)*"X"
else:
    result = tens*"X"

# такие же условия, только для единиц (прошыле были для десятков)
if units == 9:
    result += "IX"
elif units == 4:
    result += "IV"
elif units >= 5:
    result += "V" + (units - 5)*"I"
else:
    result += units*"I"

# выводим результат
print(result)
