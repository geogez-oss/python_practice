a = float(input())
b = float(input())
print(0.5 * a * b)

n = float(input())
if n != 0:
    print(1 / n)
else:
    print('Обратного числа не существует')

tf = float(input())
t = (5 / 9) * (tf - 32)
print(t)

age = float(input())
x = age - 2
age_1 = age - x
if 1 <= age <= 2:
    print(age * 10.5)
else:
    print(int((x * 4) + age_1 * 10.5))

n = float(input())
x = int((n * 10) % 10)
print(x)

n = float(input())
x = n % 1
print(x)

x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())
x5 = int(input())
print(f'Наименьшее число = {min(x1, x2, x3, x4, x5)}')
print(f'Наибольшее число = {max(x1, x2, x3, x4, x5)}')

x1 = float(input())
x2 = float(input())
x3 = float(input())
x4 = float(input())
x5 = float(input())
print(abs(x1) + abs(x2) + abs(x3) + abs(x4) + abs(x5))


x1 = int(input())
n1 = (x1 // 100) % 100
n2 = (x1 // 10) % 10
n3 = x1 % 10
digits = [n1, n2, n3]
digits.sort()
if digits[2] - digits[0] == digits[1]:
    print('Число интересное')
else:
    print('Число неинтересное')

x1 = int(input())
x2 = int(input())
x3 = int(input())
sum_all_digits = (x1 + x2 + x3)
summa_min_max = min(x1, x2, x3) + max(x1, x2, x3)
print(max(x1, x2, x3), sum_all_digits - summa_min_max, min(x1, x2, x3), sep='\n')

p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())
print(abs(p1 - q1) + abs(p2 - q2))

