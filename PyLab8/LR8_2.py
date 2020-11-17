print("Enter a:")
a = float(input())
print("Enter n:")
n = int(input())

P = 1
for i in range(0, n+1):
    P *= a - i*n

print("P =", P)