
# Я решил 12й вариант сделать
array = []
array1 = []
array2 = []
a = ""
sum = 0

print("Enter first array ( . is end):")
while (a != "."):
    a = input()
    if(a != "."):
        array.append(float(a))
        sum += float(a)

average = sum / len(array)

for i in array:
    if (i <= average):
        array1.append(i)
    else:
        array2.append(i)

print(array1)
print(array2)