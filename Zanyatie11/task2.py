#Значениями словаря могут быть и списки.
#Создайте словарь с ключами BMW, Tesla и списками из 3х моделей в качестве значений.
#Выведите первое и последнее значения каждого из ключей.
cars = { 'BMW': ['X3', 'X5', 'X6'], 'Tesla': ['Model 3', 'Model S', 'Model X']}
print(cars['BMW'][0::2], cars['Tesla'][0::2])