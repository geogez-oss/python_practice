city_1 = input()
city_2 = input()
city_3 = input()
len_1 = len(city_1)
len_2 = len(city_2)
len_3 = len(city_3)
if len_1 <= len_2 and len_1 <= len_3:
    print(city_1)
elif len_3 <= len_1 and len_3 <= len_1:
    print(city_3)
else:
    print(city_2)
if len_1 >= len_2 and len_1 >= len_3:
    print(city_1)
elif len_3 >= len_2 and len_3 >= len_1:
    print(city_3)
else:
    print(city_2)
str1 = len(input())
str2 = len(input())
str3 = len(input())
max_length = max(str1, str2, str3)
min_length = min(str1, str2, str3)
mid = (str1 + str2 + str3) - max_length - min_length
if max_length - mid == mid - min_length:
    print('YES')
else:
    print('NO')

color = input()
if 'синий' in color:
    print('YES')
else:
    print('NO')

day = input()
if 'суббота' in day or 'воскресенье' in day:
    print('YES')
else:
    print('NO')

email = input()
if '@' in email and '.' in email:
    print('YES')
else:
    print('NO')
