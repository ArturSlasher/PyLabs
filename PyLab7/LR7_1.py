# Задание 1
print("Enter a:")
a= float(input())
print("Enter b:")
b = float(input())
print("Enter c:")
c = float(input())

isOpposite = False
if (a == -b or a == -c or b == -c):
    isOpposite = True

print(isOpposite)