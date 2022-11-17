#Дан список. Все числа этого списка проверить на чётность. Если число чётное, то посчитать сумму его цифр.
#Если нечётное, то заменить  его на 1 в списке. Все слова: посчитать количество гласных и согласных. Вывести всё на экран.
list = [15, 48, 'hello', 6, 19, 'world']
list1 = [q for q in list if type(q) != str]
list2 = [q for q in list if type(q) != int]
print(list1)
print(list2)
a1 = a2 = 0
for i in list1:
    if i % 2 == 0:
        print(sum(a2))
        a1 += i
    else:
        list[0] = 1
print(a1)
print(a2)

