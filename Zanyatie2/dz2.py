a = float(input("Введите длину первого катета"))
b = float(input("Введите длину второго катета"))
c = float(input("Введите длину гипотенузы")) #Можно было определить через math.hypot, но тогда не проверить равносторонний
a1 = float(input("Введите угол a"))
b1 = float(input("Введите угол b"))
c1 = float(input("Введите угол c"))
if a + b > c or a + c > b or b + c > a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")
if a == b and a == c:
    print("Треугольник равносторонний")
    if a1 == 60 and b1 == 60 and c1 == 60:
        print("Остроугольный")
elif a != b and a != c and b != c:
    print("Треугольник разносторонний")
    if a1 >= 60 and a1 < 90 and b1 >= 60 and b1 < 90 and c1 >= 60 and c1 < 90:
        print("Остроугольный")
    elif a1 > 90 or b1 > 90 or c1 > 90:
        print("Тупоугольный")
    elif b1 == 90:
        print("Прямоугольный")
else:
    print("Треугольник равнобедренный")
    if a1 == c1 and b1 < 90:
        print("Остроугольный")
    elif b1 > 90:
        print("Тупоугольный")
    elif a1 == 45 and c1 == 45:
        print("Прямоугольный")





