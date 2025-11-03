from re import*
s = input("Введите числа через пробел: ")
sp = [int(i) for i in s.split()]

sp2 = []
for i in range(len(sp)):
    min1 = 10**20
    p = 10**20
    for k in range(len(sp)):
        if i!=k:
            if abs(sp[i]-sp[k])<=min1:
                min1 = abs(sp[i]-sp[k])
                p = sp[k]
            if abs(sp[i]-sp[k])==min1 and sp[k]<p:
                p = sp[k]

    sp2.append(str(p))

print(' '.join(sp2))