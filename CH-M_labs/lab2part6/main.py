k1 = float(input("Enter k1: "))
p1 = float(input("Enter p1: "))
k2 = float(input("Enter k2: "))
p2 = float(input("Enter p2: "))

resultK = k1 + k2
percentage1 = k1 / (k1 + k2)
percentage2 = 1 - percentage1
resultP = percentage1*p1 + percentage2*p2
print(resultK, "килограмм по", resultP)