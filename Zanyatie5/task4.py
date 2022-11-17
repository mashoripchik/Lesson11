a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
while a < 0:
    a += 1
    if a == 0:
        break
    print(a)
while b < 0:
    b += 1
    if b == 0:
        break
    print(b)