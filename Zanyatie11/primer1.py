d = {}
d = {'dict': 1, 'dictionary': 2}
print(d)
#списки не могут быть ключами. словари неизменяеммый тип данных

d = dict(short = 'dict', long = 'dictionary') # в методе дикт не может быть цифр, только строковые значения
d_2 = dict([(1, 1), (2, 4)])
print(d, '\n', d_2)

d = dict.fromkeys(['a', 'b'])
d_2 = dict.fromkeys(['a', 'b'], 100)
print(d, '\n', d_2)

d = {a: a ** 2 for a in range(7)}
print(d)

d = {1: 2, 2: 4, 3: 9} # можем обращаться к ним через срезы
d[4] = 4 ** 2
print(d[1])
print(d)

