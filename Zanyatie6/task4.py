#Даны 2 списка. Выполнить следующие операции:
a = [4, 6, 'py', 78]
b =[44, 'hello', 56, 'exept', 3]
#Сложить два списка;
print(a + b)
#Добавьте элемент 6 на 3 позицию в 2м списке
b.insert(2, 6)
print(b)
# Удалите все текстовые переменные;
print([i for i in a if type(i) != str])
print([f for f in b if type(f) != str])
#Посчитайте количество элементов списка.
print(len(a))
print(len(b))
