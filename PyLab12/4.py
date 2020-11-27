L = [1, 6, -3, 5, -22]

for i in range(len(L)-1):
    if L[i] < 0:
        L.pop(i)

print(L)