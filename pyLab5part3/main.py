a = 963

firstNum = a // 100
secondSum = a // 10 - firstNum * 10
thirdNum = a % 10

result = firstNum + secondSum + thirdNum
print(result)
