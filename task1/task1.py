import math

n = int(input()) #размер массива
m = int(input()) #длина обхода
traversals = [] #обходы
sample = [i for i in range(1, n + 1)]

while True:
    if len(traversals) >= 1 and traversals[-1][-1] == traversals[0][0]:
        break
    else:
        if m <= n: #если шаг меньше длины массива
            if len(traversals) == 0:
                traversals.append(sample[:m])
            else:
                mult = 2
                tmp = sample*mult
                start = tmp.index(traversals[-1][-1])
                traversals.append(tmp[start:start + m])
        elif m > n: #если шаг больше длины массива
            if len(traversals) == 0:
                mult = math.ceil(m/n)
                tmp = sample*mult
                traversals.append(tmp[:m])
            else:
                tmp = sample*mult*2
                start = tmp.index(traversals[-1][-1])
                traversals.append(tmp[start:start + m])

print(*[i[0] for i in traversals], sep='')
