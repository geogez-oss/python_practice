from math import *

R = float(input())
print(pi * pow(R, 2))
print(2 * pi * R)

from math import *
n = float(input())
print(ceil(n) + floor(n))

from math import *
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
p = sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))
print(p)

from math import *

x1 = float(input())
print(sin(radians(x1)) + cos(radians(x1)) + pow(tan(radians(x1)), 2))

from math import *

n = int(input())
a = float(input())
S = (n * pow(a, 2)) / (4 * tan(pi / n))
print(S)

from math import *

a = float(input())
b = float(input())
mid_aref = (a + b) / 2
mid_geo = sqrt(a * b)
mid_garm = (2 * a * b) / (a + b)
mid_sqrt = sqrt((pow(a, 2) + pow(b, 2)) / 2)
print(mid_aref, mid_geo, mid_garm, mid_sqrt, sep='\n')

from math import *

a = float(input())
b = float(input())
c = float(input())

D = pow(b, 2) - 4 * a * c

if D < 0:
    print('Нет корней')
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    x1 = (-b - sqrt(D)) / (2 * a)
    x2 = (-b + sqrt(D)) / (2 * a)
    print(min(x1, x2), max(x1, x2), sep='\n')