from random import random, randint

n = random() * 900 + 100
n = int(n)
print(n)
a = n // 100
b = (n // 10) % 10
c = n % 10
print(a + b + c)

a1 = randint(100, 999)
print(a1)
a2 = a1 // 100
b1 = (a1 // 10) % 10
c1 = a1 % 10
print(a2 + b1 + c1)

