#9.50
str1 = "Artur delaet labu"
str2 = "Vasya"
newStr = ""

for i in range(len(str1)):
    if (i < len(str2)):
        newStr += str2[i]
    else:
        newStr += str1[i]

print(newStr)