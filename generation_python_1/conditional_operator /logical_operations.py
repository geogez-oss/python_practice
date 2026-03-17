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