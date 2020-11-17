array = []
a = ""

print("Enter first array ( 0 is end):")
while (a != "0"):
    a = input()
    if(a != "0"):
        array.append(a)

print("Quantity of elements:", len(array))