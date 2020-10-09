a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))
e = float(input("e: "))
arr = [a, b, c, d, e]
currMin = arr[0]
currMinIndex = 0
for i in arr:
    if i < currMin:
        currMin = i
        currMinIndex = arr.index(i)
print(currMin, "is min and has index", currMinIndex)