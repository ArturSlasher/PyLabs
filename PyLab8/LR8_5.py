array1 = []
array2 = []
a = ""
coincidenceSum = 0

print("Enter first array ( . is end):")
while (a != "."):
    a = input()
    if(a != "."):
        array1.append(a)

print("Enter second array:")
for i in range(len(array1)):
    a = input()
    array2.append(a)

for i in range(len(array1)):
    if (array1[i] == array2[i]):
        coincidenceSum += 1

print("Number of coincidences =", coincidenceSum)