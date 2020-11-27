import random

print("How many numbers do you want?")
n = int(input())
f = open('4.txt', 'w')
numberList = []
for i in range(n):
     numberList.append(random.randint(1, 1000))
     f.write(str(numberList[i]) + " ")
f.close()
print(numberList)

print("Enter an end-number:")
endNumber = int(input())
numbersSum = 0
for num in numberList:
    if num % 10 == endNumber:
        numbersSum += num

print(numbersSum)
f.close()