#Циклы 1. Введение в циклы; 2. Цикл For; 3. Модуль array. Массивы в python
# цикл For и цикл while

#primer1
for i in range(4):
    print(i)
for s in range(4, 8):
    print(s)

#primer2
for n in "Я учу Python":
    print(n)

#primer3
for h in range(15, 0, -1):
    print(h)

#primer4 Модуль array. Тип данных "Список" или по другому "Массив"
arr = []
arr = ['string1', 'string2', 'string3']
l = len(arr)
print(arr, 'Длина: ', l)

#primer5 Применение цикла for в массиве array
for p in arr:
    print(p)

#primer6 оператор break досрочно прерывает цикл, либо условие
arr = [1, 7, 9, 10]
for t in arr:
    print(t)
    if t == 9:
        break

#primer7 оператор  Continue. Этот оператор начинает следующий проход цикла, минуя оставшееся тело цикла
for k in arr:
    if k == 9:
        continue
    print(k)

#primer8 Добавление элемента. Имя массива.append(значение)
a = [10, 3, 3]
print(a)
a.append(7)
print(a)

#array.append(x) - добавление элемента в конец массива
#array.count(x) - возвращает количество вхождений x в массив
#array.index(x) - удаляет i-ый элемент

