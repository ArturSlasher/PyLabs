import math

def euclidDistance(xA, yA, zA, xB, yB, zB):
    return math.sqrt(pow((xA - xB), 2) + pow((yA - yB), 2) + pow((zA - zB), 2))

print(euclidDistance(1,1,1,4,1,1))
