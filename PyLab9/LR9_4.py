# 8 вариант - з
print("Enter n:")
n = int(input())
currentN = n
currentI = -1
currentJ = 0
buffBool = True
if (n % 2 == 0):
    isEven = True
else:
    isEven = False

matrix = [[0 for y in range(n)] for x in range(n)]

for j in range(n):
    # заполняем единицами по столбцам
    currentI += 1
    for i in range(currentN):
        if (currentI < n and currentJ < n):
            matrix[currentJ][currentI] = 1
            currentJ += 1
    currentJ -= currentN
    if (currentI < n / 2-1):
        # если не прошли половину матрицы, то единицы "сужаются"
        currentN -= 2
        currentJ += 1
    else:
        # если прошли половину матрицы, то единицы "расширяются"
        if (isEven and buffBool):
            # это нужно на случай, если N - чётное
            buffBool = False
        else:
            currentN += 2
            currentJ -= 1

for i in matrix:
    print(i)