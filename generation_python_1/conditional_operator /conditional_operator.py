s = input()
s1 = input()
if s==s1:
    print('Пароль принят')
else:
    print('Пароль не принят')


n = int(input())
if n % 2 == 0:
    print('Четное')
else:
    print('Нечетное')

age = int(input())
if age < 18:
    print('Доступ запрещен')
else:
    print('Доступ разрешен')

a = int(input())
b = int(input())
if a < b:
    print(a)
elif b < a:
    print(b)
else:
    print(a)

a = int(input())
b = int(input())
c = int(input())

if b - a == c - b:
    print('YES')
else:
    print('NO')

n = int(input())
x1 = n // 1000
x2 = n // 100 % 10
x3 = n // 10 % 10
x4 = n % 10
if x1 + x4 == x2 - x3:
    print('ДА')
else:
    print('НЕТ')

