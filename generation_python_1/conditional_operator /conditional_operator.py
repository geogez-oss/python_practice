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

a = int(input())
b = int(input())
c = int(input())
count = 0
if a > 0:
    count += a
if b > 0:
    count += b
if c > 0:
    count += c
print(count)

age = int(input())
if age <= 13:
    print('детство')
if 14 <= age <= 24:
    print('молодость')
if 25 <= age <= 59:
    print('зрелость')
if age >= 60:
    print('старость')

a = int(input())
b = int(input())
c = int(input())
d = int(input())

min_value = a
if b < a:
    min_value = b
if c < b:
    min_value = c
if d < c:
    min_value = d
print(min_value)