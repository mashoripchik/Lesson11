arr = ["Картошка", "Гречка", "Грибы", "Суп"]
a = input("Введите блюдо: ")
for b in arr:
    if b == a:
        print('Я не ем ' + a)
        break
    print("Отлично вкусный " + b)
else:
    print("Спасибо за ужин")

print("Вкусный ужин")





