print("Enter a:")
a= float(input())
print("Enter b:")
b = float(input())
print("Enter c:")
c = float(input())

positiveSum = 0
if (a > 0):
    positiveSum += 1
if (b > 0):
    positiveSum += 1
if (c > 0):
    positiveSum +=1

print("Number of positive:", positiveSum)