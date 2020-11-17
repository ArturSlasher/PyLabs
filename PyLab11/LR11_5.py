#9.82
str = " moloko uzhe zakipaet"
count = 0
if (str[0] != " "):
    i = 0
else:
    i = 1

while (str[i] != " "):
    if (str[i] == "o"):
        count += 1
    i += 1

print("Number of O's:", count)