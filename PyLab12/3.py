list = ['w', 'o', 'r', 'd', ' ', 't', 'h', 'a', 't', ' ', 'i', 's', ' ',
        'u', 's', 'e', 'd', ' ', 'i', 'n', ' ', 'a', 'l', 'g', 'o', 'r', 'i', 't', 'h', 'm', ' ',
        'f', 'i', 'n', 'd', 'i', 'n', 'g', ' ', ' ', 'w', 'o', 'r', 'd']

print(list)
for i in range(len(list)):
    if (i < len(list)-3 and list[i] == 'w' and list[i+1] == 'o' and list[i+2] == 'r' and list[i+3] == 'd'):
        print("We found 'word' with start index", i)