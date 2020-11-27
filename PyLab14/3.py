wordList = []
f = open("3.txt", 'r')
text = f.read()

wordInteger = 0
wordList.append("")
for letter in range(len(text)):
    if text[letter] != " " and text[letter] != "-" and text[letter] != "," and text[letter] != ".":
        wordList[wordInteger] += text[letter]
    else:
        wordInteger += 1
        wordList.append("")

wordList.sort()
for word in wordList:
    if word != '':
        print(word)