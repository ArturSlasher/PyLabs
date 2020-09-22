import math

def isSquare(xA, yA, xB, yB, xC, yC, xD, yD):
    AB = math.sqrt(pow((xB - xA), 2) + pow((yB - yA), 2))
    BC = math.sqrt(pow((xC - xB), 2) + pow((yC - yB), 2))
    CD = math.sqrt(pow((xD - xC), 2) + pow((yD - yC), 2))
    AD = math.sqrt(pow((xD - xA), 2) + pow((yD - yA), 2))
    BD = math.sqrt(pow((xD - xB), 2) + pow((yD - yB), 2))
    AC = math.sqrt(pow((xC - xA), 2) + pow((yC - yA), 2))

    if AB == BC and AB == CD and AB == AD and BD == AC:
        return True
    else:
        return False

print(isSquare(0, 0, 2, 5, 4, 0, 2, -5))
