#primer1
i = 0
while i < 10:
    print(i)
    i = i + 1  # i + 1 это count (счетчик), он может быть как в конце, так и в начале и середине. Обычно ставят в конце

#primer 2
a = 0
while a < 10:
    print(a)
    if a == 5:
        break
    a += 1

#primer3 Вывести сумму чисел от 1 до 50 и результат вывести на экран
b = 1
result = 0
while b <= 50:
    result += b
    b += 1
print(result)
