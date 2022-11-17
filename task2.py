import math
a = int(input("Введите длину первого катета"))
b = int(input("Введите длину второго катета"))

print('Периметр равен:', a+b+math.hypot(a,b))
print('Площадь равна:', a*b/2)
