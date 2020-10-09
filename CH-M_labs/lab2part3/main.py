import math
x = float(input("Enter x: "))
if (x > 5):
    y1 = math.sqrt(2*x/(x-5))
    y2 = (math.sqrt(2*x)-math.sqrt(x-5)) / (math.sqrt(2*x)+math.sqrt(x-5))
    y3 = (math.sqrt(2*x)+math.sqrt(x-5)) / (math.sqrt(2*x)-math.sqrt(x-5))
    y = y1 / (y2 - y3)
    print(y)
else:
    print("Invalid enter")