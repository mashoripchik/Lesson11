#Дан список некоторых целых чисел, найдите значение 20 в нем и, если оно присутствует, замените его на 200
#Обновите список только при первом вхождении числа 20.
arr = [1, 5, 10, 15, 20, 25, 30, 20, 35]
b = arr.index(20)
print(arr)
if 20 in arr:
    arr.insert(b, 200)
    print(arr)
    arr.remove(20)
    print(arr)
