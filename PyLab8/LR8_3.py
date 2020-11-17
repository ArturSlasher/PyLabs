print("Enter S:")
S = float(input())

resultSum = 0
for i in range(100):
    a = 1 / 2 ** i + 1 / 3 ** i
    if (abs(a) >= S):
        resultSum += a

print("Result sum:", resultSum)