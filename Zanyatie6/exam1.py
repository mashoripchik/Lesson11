import random
i = random.randint(0, 10)
a = 1
while True:
    if i == 10:
        break
    else:
        i = i + a
        print(i)
print(f'Количество попыток {a}')

for i in range(11):
    if i == 10:
        break
    else:
        i += 1
        print(i)



