# вводим числа x1, y1, x2, y2 с клавиатуры
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# TRUE - если число положительное, иначе FALSE
signx1 = x1 > 0
signy1 = y1 > 0
signx2 = x2 > 0
signy2 = y2 > 0

# чтобы точки были в одной четверти, у них должны быть координаты x и y соответственно одинакового знака
# если хотя бы одна координата не сходится по знакам, то NO, иначе YES
if (signx1 != signx2) or (signy1 != signy2):
    print("NO")
else:
    print("YES")
