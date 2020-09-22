import math
import random

x = random.uniform(-2,2)
print(x)

y = 228
if x < 0:
    y = math.cos(x)
if x < 1.5:
    y = pow(x, 3) + 2*pow(x, 2) + 1
else:
    y = 0

print(round(y, 3))
