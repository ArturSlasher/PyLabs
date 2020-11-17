#9.97
str = "eight bits equals one byte. This is bitnary informatics"
str1 = ""
strIt = 0

for i in str:
    if (strIt >= len(str)):
        break
    if (str[strIt]== "b" and str[strIt + 1]== "i" and str[strIt + 2]== "t"):
        str1 += "rog"
        strIt += 2
    else:
        str1 += str[strIt]
    strIt += 1

print(str1)