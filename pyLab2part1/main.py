a = 33
firstNumber = (a - a%10) / 10
secondNumber = a%10

if (firstNumber%2==0 and secondNumber%2!=0) or (firstNumber%2!=0 and secondNumber%2==0):
    print("Yes")
else:
    print("No")
