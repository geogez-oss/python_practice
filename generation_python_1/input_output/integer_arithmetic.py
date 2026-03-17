x = int(input())
x1 = x + 1
x2 = x1 + 1
print(x, x1, x2, sep='\n')

a = int(input())
b = int(input())
c = int(input())
print(sum((a, b, c)), end='')

count = 0
for n in range(4):
    n = int(input())
    count += n
print(count * 3)

a = int(input())
b = int(input())
print(3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41)

n = int(input())
print(f'Следующее за числом {n} число: {n + 1}')
print(f'Для числа {n} предыдущее число: {n - 1}')

a = int(input())
print(f'Объем = {a ** 3}')
print(f'Площадь полной поверхности = {6 * a ** 2}')

a, d, n = int(input()), int(input()), int(input())
print(a + d * (n - 1))

x = int(input())
print(x, x * 2, x * 3, x * 4, x * 5, sep='---')

b = int(input())
q = int(input())
n = int(input())
print(b * q ** (n - 1))

sm = int(input())
print(sm // 100)

n = int(input())
k = int(input())
x = k // n
y = k % n
print(x, y, sep='\n')

n = int(input())
print((n + 1) // 2)

m = int(input())
print(f'{m} мин - это {m // 60} час {m % 60} минут')

n = int(input())
x = (n + 3) // 4
print(x)

n = int(input())
x1 = n % 10
x2= n // 10 % 10
x3= n // 100 % 10
print(f'Сумма цифр = {sum([x1, x2, x3])}')
print(f'Произведение цифр = {x1 * x2 * x3}')

n = int(input())
x1 = str(n % 10)
x2 = str(n // 10 % 10)
x3 = str(n // 100 % 10)
print(x3, x2, x1, sep='')  # ← вот это не хватало
print(x3, x1, x2, sep='')
print(x2, x3, x1, sep='')
print(x2, x1, x3, sep='')
print(x1, x3, x2, sep='')
print(x1, x2, x3, sep='')

n = int(input())
x1 = n // 1000 % 10
x2 = n // 100 % 10
x3 = n // 10 % 10
x4 = n % 10
print(f'Цифра в позиции тысяч равна {x1}')
print(f'Цифра в позиции сотен равна {x2}')
print(f'Цифра в позиции десятков равна {x3}')
print(f'Цифра в позиции единиц равна {x4}')n = int(input())
x1 = n // 1000 % 10
x2 = n // 100 % 10
x3 = n // 10 % 10
x4 = n % 10
print(f'Цифра в позиции тысяч равна {x1}')
print(f'Цифра в позиции сотен равна {x2}')
print(f'Цифра в позиции десятков равна {x3}')
print(f'Цифра в позиции единиц равна {x4}')