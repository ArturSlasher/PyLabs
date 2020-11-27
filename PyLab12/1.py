print("Enter N:")
n = int(input())
list = [n]
print("Enter elements:")
for i in range(n):
    list.append(int(input()))

for i in range(len(list)):
    if (list[i] == 22):
        list.insert(i, 0.99)
        break

print(list)