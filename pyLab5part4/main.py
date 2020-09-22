import math

x = 1.
y = -1.

result1 = math.sqrt(1 + (1 + math.log(pow(x, 2))))
result2 = math.sqrt(1 + 1 / (1 + abs(y)))
result3 = 2 * x * (1 + pow(y , 2))
z = (result1 + result2) / result3
print(round(z, 2))
