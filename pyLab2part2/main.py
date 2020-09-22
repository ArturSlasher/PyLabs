import math

x = 2
y = 2
z = 5.3

F = max(x+y, z) / min(x, y+z)
if math.modf(F)[0] < 0.5:
    F = F - math.modf(F)[0]
else:
    F = F + (1 - math.modf(F)[0])
print(F)
