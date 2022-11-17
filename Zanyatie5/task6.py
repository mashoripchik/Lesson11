a1 = float(input("Введите первое число: "))
a2 = input("Введите арифметическую операцию (+-/*): ")
a3 = float(input("Введите второе число: "))
while a2 == '+':
    a1 = a1 + a3
    print(a1)
    break
while a2 == '-':
    a1 = a1 - a3
    print(a1)
    break
while a2 == '*':
    a1 = a1 * a3
    print(a1)
    break
while a2 == '/':
    if a3 == 0:
        break
    a1 = a1 / a3
    print(a1)
    break



