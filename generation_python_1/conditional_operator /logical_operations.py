number = int(input())
if -1 < number and number < 17:
    print('Принадлежит')
else:
    print('Не принадлежит')

number = int(input())
if number <= -3 or number >= 7:
    print('Принадлежит')
else:
    print('Не принадлежит')


number = int(input())
if  -30 < number <= -2  or 7 < number <= 25:
    print('Принадлежит')
else:
    print('Не принадлежит')

number = int(input())
if (number % 7 == 0 or number % 17 == 0) and len(str(number)) == 4:
    print('YES')
else:
    print('NO')

a = int(input())
b = int(input())
c = int(input())
if a + b > c and a + c > b and b + c > a:
    print('YES')
else:
    print('NO')

year = int(input())
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('YES')
else:
    print('NO')

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 == x2 or y1 == y2:
    print('YES')
else:
    print('NO')

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if (x1 == x2 or x1 == x2 + 1 or x1 == x2 - 1) and (y1 == y2 or y1 == y2 + 1 or y1 == y2 - 1):
    print('YES')
else:
    print('NO')

n = int(input())
k = int(input())
if n > k:
    print('NO')
elif n < k:
    print('YES')
else:
    print("Don't know")

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('Равносторонний')
elif a == b or b == c or a == c:
    print('Равнобедренный')
else:
    print('Разносторонний')

a = int(input())
b = int(input())
c = int(input())

if b <= a <= c or c <= a <= b:
    median = a
elif a <= b <= c or c <= b <= a:
    median = b
else:
    median = c

print(median)

mounth = int(input())
if mounth in [1, 3, 5, 7, 8, 10, 12]:
    print(31)
elif mounth in [4, 6, 9, 11]:
    print(30)
else:
    print(28)

weight = int(input())
if weight < 60:
    print('Легкий вес')
elif 60 <= weight < 64:
    print('Первый полусредний вес')
elif 64 <= weight < 69:
    print('Полусредний вес')

a = int(input())
b = int(input())
op = input()

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b == 0:
        print("На ноль делить нельзя!")
    else:
        print(a / b)
else:
    print("Неверная операция")

color1 = input().lower()
color2 = input().lower()

colors = {color1, color2}
main_colors = {"красный", "синий", "желтый"}

# Проверяем, что оба цвета основные
if not colors.issubset(main_colors):
    print("ошибка цвета")
elif color1 == color2:
    print(color1)  # Если смешать одинаковые, цвет не изменится
elif "красный" in colors and "синий" in colors:
    print("фиолетовый")
elif "красный" in colors and "желтый" in colors:
    print("оранжевый")
elif "синий" in colors and "желтый" in colors:
    print("зеленый")

n = int(input())

if n < 0 or n > 36:
    print("ошибка ввода")
elif n == 0:
    print("зеленый")
elif 1 <= n <= 10 or 19 <= n <= 28:
    if n % 2 != 0:
        print("красный")
    else:
        print("черный")
elif 11 <= n <= 18 or 29 <= n <= 36:
    if n % 2 != 0:
        print("черный")
    else:
        print("красный")

a1 = int(input())
b1 = int(input())
a2 = int(input())
b2 = int(input())

if a1 < b1 < a2 < b2 or a2 < b2 < a1 < b1:
    print('пустое множество')

elif a2 < a1 < b1 < b2:
    print(a1, b1)

elif a2 < a1 < b2 < b1:
    print(a1, b2)

elif a1 < a2 < b1 < b2:
    print(a2, b1)

elif a1 < a2 < b2 < b1:
    print(a2, b2)

elif b2 == a1:
    print(a1)

elif b1 == a2:
    print(a2)

elif a1 == a2 and b1 == b2:
    print(a1, b1)

elif a2 < a1 and b1 == b2:
    print(a1, b1)

elif a1 < a2 and b1 == b2:
    print(a2, b2)

elif a1 == a2 and b1 < b2:
    print(a1, b1)

elif a1 == a2 and b2 < b1:
    print(a2, b2)

else:
    print('пустое множество')