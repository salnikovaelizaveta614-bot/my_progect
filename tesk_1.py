n = int(input("Введите количество чисел, которые хотите ввсети: "))
print("Введите числа: ")
sp = []
for i in range (n):
    sp.append(int(input()))

sp2 = []
for i in range(n):
    min1 = 10**20
    p = 10**20
    for k in range(n):
        if i!=k:
            if abs(sp[i]-sp[k])<=min1:
                min1 = abs(sp[i]-sp[k])
                p = sp[k]
            if abs(sp[i]-sp[k])==min1 and sp[k]<p:
                p = sp[k]

    sp2.append(str(p))

print(' '.join(sp2))