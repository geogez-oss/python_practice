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
