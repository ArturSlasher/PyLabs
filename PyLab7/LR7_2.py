import math

print("Enter point coordinate X:")
x = int(input())
print("Enter point coordinate Y:")
y = int(input())

rBig = 6
rSmall = 4

hypotenuse = math.sqrt(x ** 2 + y ** 2)

if hypotenuse <= rBig and hypotenuse >= rSmall and y >= 2:
    print(True)
else:
    print(False)