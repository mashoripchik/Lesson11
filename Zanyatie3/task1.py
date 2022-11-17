#Primer1
a = 'I Love \ Python'
b = 'I Love \' Python\''
c = 'I Love \" Python\"'
d = 'I Love \n Python\n'
e = 'I\tLove\tPython'
print(a + '\n\r' + b + '\n\r' + c + '\n\r' + d)
#Primer2
name = 'John'
age = 20
print(f'Name {name}, age {age}!')
#primer3
str = 'Строка'
str2 = ' одна'
print(str + str2)
#primer4
string = 'Hello world'
st = 'Hello'
print(st in string)
#primer5
print(ord("a"))
#primer6
s = 'Hello'
#print(s[0], s[4], s[-5])
#print(s[0:4], s[1:3], s[1:])
print(s[0:5:1], s[::-1], s[0:5:2], s[::2])
#primer7
j = "true"
print(j.upper())
#primer8
print('A'.isdigit())   #Проверка состоит ли строка из цифр  (True / False)
print('A'.isalpha())   #Проверка состоит ли строка из букв  (True / False)
#primer9
print('..'.join(['a', 'b']))
print('1_2_3'.split('_'))
#primer10 метод .replace()
#s.replace(' ', '')