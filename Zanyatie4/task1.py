a = input("Введите строку: ")
b = input("Введите символ: ")
for i in a:
    if i == b:
        continue
    else:
        print(i, end = '')