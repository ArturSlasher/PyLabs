import random

print("Enter N:")
n = int(input())
f1 = open('1.txt', 'w')
buffVar = 1
numberList = []
for i in range(n):
     numberList.append(random.randint(1, 1000))
     f1.write(str(numberList[i]) + " ")
f1.close()

f1 = open('1.txt', 'r')
f2 = open('1result.txt', 'w')
for j in range(n):
     buffVar *= numberList[j]
     f2.write(str(buffVar) + " ")

f1.close()
f2.close()