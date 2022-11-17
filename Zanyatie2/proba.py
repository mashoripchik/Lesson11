import random
print('Введите кол-во N ')
N=int(input())
a=list()
for i in range (0,N):
  a.append(random.randint(0,20))
print('Массив',a,"\n")
min=a[0]
for i in range(len(a)):
  if (a[i] < min):
    min = a[i]
    k=i
print ('Минимальное значение: ',min)
sum = 0
for i in range(min+1,i<N):
    sum += a[i]
    i += 1
print('Сумма равна '+' '+str(sum))