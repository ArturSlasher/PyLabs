import math

def compareABC(xA, yA, xB, yB, xC, yC):
    AB = math.sqrt(pow((xB - xA), 2) + pow((yB - yA), 2))
    BC = math.sqrt(pow((xC - xB), 2) + pow((yC - yB), 2))
    AC = math.sqrt(pow((xC - xA), 2) + pow((yC - xA), 2))

    if AB > BC and AB > AC:
        return "AB"
    if BC > AB and BC > AC:
        return "BC"
    if AC > AB and AC > BC:
        return "AC"
    else: return 0

print(compareABC(1, 1, 5, 5, 9, 0))
