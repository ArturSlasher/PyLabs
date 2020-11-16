import math

print("Enter x:")
x = float(input())

if (x > -25 and x <= -18):
    F = 6 * math.sqrt(abs(x))
elif (x > -18 and x <= 7):
    F = math.log(abs(x))
elif (x > 7 and x <= 14):
    F = 1 / x
else:
    F = 8

print("Result is", F)