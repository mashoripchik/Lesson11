#zadanie1
name = input('Введите ваше имя')
print(f'Привет, {name}!')
print(3*name)

#zadanie2 Вычислить сумму цифр случайного трёхзначного числа при помощи срезов
a = input("Введите случайное трёхзначное число: ")
b = int(a[0])
c = int(a[1])
e = int(a[2])
print("Сумма цифр случайного трёхзначного числа: ", b + c + e)

#zadanie3 На вход подается непустая строка S
s = input("Введите строку состоящую хотя бы из двух символов: ")
    #1) В первой строке распечатайте каждый 3-й символ, начиная с нулевого (подряд, не разделяя символы пробелами).
print(s[::3])
    #2) Во второй строке распечатайте первый и последний символы (подряд, не разделяя символы пробелами).
print(s[:1] + s[-1:])
    #3) В третей строке распечатайте S в верхнем регистре.
print(s.upper())
    #4) В четвертой строке распечатайте S в обратном порядке.
print(s[::-1])
    #5) В пятой строке напечатайте True, если все символы в строке S — цифры и False в противном случае.
print('S'.isdigit())

#zadanie4 Вводиться строка. Удалить из неё все пробелы. После этого определить, является ли она палиндромом(перевертышем)
j = input("Введите строку: ")
print(''.join(j.split())) #1 способ
print(j.replace(" ","")) #2 способ
if j[::1] == j[::-1]:
    print('Строка является палидромом')
else:
    print('Строка не является палидромом')