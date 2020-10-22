
##########################
sA = "ijfexo76ijfaoifa9843029jfa"
sAresult = ""
for i in sA:
    if i.isnumeric():
        sAresult += "*"
    else:
        sAresult += i
print("A:", sAresult)
##########################

sB = "2 56 1"
sum = 0
for i in sB.split(" "):
    sum += int(i)
print("B:", sum)
##########################

sC = "23+14"
resultC = int(sC.split("+")[0]) + int(sC.split("+")[1])
sC += "=" + str(resultC)
print("C:", sC)
##########################

sE = "+38(095)4874283"
sEresult = ""
for i in range(len(sE)):
    if sE[i]=="(":
        sEresult += sE[i+1] + sE[i+2] + sE[i+3]
print("E:", sEresult)
##########################

alphabet = "abcdefghijklmnopqrstuvwxyz"
sF = "hello world z"
sFresult = ""
for i in range(len(sF)):
    if (sF[i] != " "):
        if (sF[i] == "z"):
            sFresult += "a"
        else:
            sFresult += alphabet[alphabet.find(sF[i])+1]
    else:
        sFresult += sF[i]
print("F:", sFresult)
##########################

sG = "hello world"
sGresult = ""
for i in range(len(sG)):
    if (sG[i] != " "):
        if (alphabet.find(sG[i])+1 < 10):
            sGresult += "0" + str(alphabet.find(sG[i])+1)
        else:
            sGresult += str(alphabet.find(sG[i])+1)
    else:
        sGresult += sG[i]
print("G:", sGresult)
##########################

sH1 = "2345 $"
sH2 = "1500 $"
sHresult = int(sH1.split(" ")[0]) + int(sH2.split(" ")[0])
print("H:", sHresult)
##########################

sI = ["109332 $", "1839 $", "2 $"]
sumI = 0
for i in sI:
    sumI += int(i.split(" ")[0])
print("I:", sumI)
##########################

sJ = "10203.02121"
sJis = False
for i in sJ:
    if i=="." or i==",":
        sJis = True
print("J:", sJis)
###########################

sK1 = "The Sun"
sK2 = "the sun"
isEqual = True
for i in range(len(sK1)):
    if (sK1[i].lower() != sK2[i].lower()):
        isEqual = False
print("K:" , isEqual, "equal")
###########################

sL = "Утречко летело к черту"
sLarr1 = sL.replace(" ", "")
sLarr2 = sLarr1[::-1]
isPalindrom = True
for i in range(len(sLarr1)):
    if (sLarr1[i].lower() != sLarr2[i].lower()):
        isPalindrom = False
print("L:", isPalindrom, "palindrom")
############################

sM = " fjdnflauf ;fdaiof;a  kjdnf;dsa "
sMresult = ""
for i in range(len(sM)-1):
    if sM[i] == " ":
        if i==0 or i==len(sM) or sM[i+1]==" ":
            continue
    sMresult += sM[i]
sMresult = "|" + sMresult + "|"
print("M:", sMresult)
############################

sN = "Kapust0chka"
isNum = False
isUp = False
isSeven = False
isCorrect = False
for i in range(len(sN)):
    if(i>=7): isSeven = True
    if(sN[i].isupper()): isUp = True
    if(sN[i].isnumeric()): isNum = True
if (isUp and isNum and isSeven): isCorrect = True
print("N:", isCorrect, "correct password")
###########################

sP = "da lfsjf fgh mlkfa"
sPresult = ""
sIterator = 0
for i in range(len(sP)):
    if (sIterator<len(sP)):
        if (sP[sIterator] == " "):
            sPresult += sP[sIterator]
        else:
            if (sIterator <= len(sP)-4 and sIterator > 0 and sP[sIterator-1] == " " and sP[sIterator+1] != " " and sP[sIterator+2] != " " and sP[sIterator+3] == " "):
                sPresult += "***"
                sIterator += 2
            else:
                sPresult += sP[sIterator]
        sIterator += 1
print("P:", sPresult)
###########################

sQ = "743207530753143"
is1 = 0
is2 = 0
is3 = 0
is4 = 0
is5 = 0
is6 = 0
is7 = 0
is8 = 0
is9 = 0
is0 = 0
for i in sQ:
    if (i == "1"): is1+=1
    if (i == "2"): is2 += 1
    if (i == "3"): is3 += 1
    if (i == "4"): is4 += 1
    if (i == "5"): is5 += 1
    if (i == "6"): is6 += 1
    if (i == "7"): is7 += 1
    if (i == "8"): is8 += 1
    if (i == "9"): is9 += 1
    if (i == "0"): is0 += 1
if (is0 > is1 and is0 > is2 and is0 > is3 and is0 > is4 and is0 > is5 and is0 > is6 and is0 > is7 and is0 > is8 and is0 > is9):
    print("Q:", 0)
elif (is1 > is0 and is1 > is2 and is1 > is3 and is1 > is4 and is1 > is5 and is1 > is6 and is1 > is7 and is1 > is8 and is1 > is9):
    print("Q:", 1)
elif (is2 > is1 and is2 > is0 and is2 > is3 and is2 > is4 and is2 > is5 and is2 > is6 and is2 > is7 and is2 > is8 and is2 > is9):
    print("Q:", 2)
elif (is3 > is1 and is3 > is2 and is3 > is0 and is3 > is4 and is3 > is5 and is3 > is6 and is3 > is7 and is3 > is8 and is3 > is9):
    print("Q:", 3)
elif (is4 > is1 and is4 > is2 and is4 > is3 and is4 > is0 and is4 > is5 and is4 > is6 and is4 > is7 and is4 > is8 and is4 > is9):
    print("Q:", 4)
elif (is5 > is1 and is5 > is2 and is5 > is3 and is5 > is4 and is5 > is0 and is5 > is6 and is5 > is7 and is5 > is8 and is5 > is9):
    print("Q:", 5)
elif (is6 > is1 and is6 > is2 and is6 > is3 and is6 > is4 and is6 > is5 and is6 > is0 and is6 > is7 and is6 > is8 and is6 > is9):
    print("Q:", 6)
elif (is7 > is1 and is7 > is2 and is7 > is3 and is7 > is4 and is7 > is5 and is7 > is6 and is7 > is0 and is7 > is8 and is7 > is9):
    print("Q:", 7)
elif (is8 > is1 and is8 > is2 and is8 > is3 and is8 > is4 and is8 > is5 and is8 > is6 and is8 > is7 and is8 > is0 and is8 > is9):
    print("Q:", 8)
elif (is9 > is1 and is9 > is2 and is9 > is3 and is9 > is4 and is9 > is5 and is9 > is6 and is9 > is7 and is9 > is8 and is9 > is0):
    print("Q:", 9)
else: print("Q: noone")
##################################

sS = "jfdsdsalkj jdck cs;asjfowei"
sSresult = sS[0].upper()
for i in range(len(sS)-1):
    if (i>0): sSresult += sS[i]
    if (sS[i] == " "):
        sSresult += sS[i+1].upper()
        i += 1
print("S:", sSresult)