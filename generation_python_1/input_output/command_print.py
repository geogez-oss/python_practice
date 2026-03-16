print('Здравствуй, мир!')
print(4, 8, 15, 16, 23, 42)
print(4, 8, 15, 16, 23, 42, sep='\n')

for i in range(1, 8):
    print(i * '*')

name = input()
print('Привет,', name)

fk = input()
print(fk, '- чемпион')

str_1 = input()
str_2 = input()
str_3 = input()
print(str_1, str_2, str_3, sep='\n')

str_1 = input()
str_2 = input()
str_3 = input()
print(str_3, str_2, str_1, sep='\n')

x, y = int(input()), int(input())
print(f'{x} + {y} = {x + y}')
print(f'{x} - {y} = {x - y}')
print(f'{x} * {y} = {x * y}')

a, d, n = int(input()), int(input()), int(input())
print(a + d * (n - 1))

x = int(input())
print(x, x * 2, x * 3, x * 4, x * 5, sep='---')
