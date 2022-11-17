s = int(input())
c = 0
for i in [25, 10, 5, 1]:
    c += s // i
    s = s % i
print(c)