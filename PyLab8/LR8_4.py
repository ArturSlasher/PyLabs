import math

print("Enter a:")
a = int(input())
print("Enter b:")
b = int(input())
print("Enter h:")
h = int(input())

print("x", "|", "F(x)")
for x in range(a, b+1, h):
    if (x != 0):
        F = math.sin(1/x) + 2
    else:
        F = 0
    print(x, "|", F)