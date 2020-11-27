print("Enter N:")
n = int(input())
list = [n]
print("Enter elements:")
for i in range(n):
    list.append(int(input()))

for i in range(len(list)):
    if (list[i] < 0):
        list.insert(i+1, 66)

print(list)