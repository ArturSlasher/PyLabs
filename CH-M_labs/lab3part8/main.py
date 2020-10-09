list = ['Inception', 'Dark Knight', 'Interstellar', 'Tenet', 'Matrix', 'Avatar']
print(list[0], list[2], list[-1], list[-2])
print(list[0:2], list[3:4], list[4:6])
manyList = [list[0:2], list[3:4], list[4:6]]
buffList = manyList[-1]
manyList[-1] = manyList[0]
manyList[0] = buffList
print(manyList)

manyList.append(['Iron man'])
print(manyList)
manyList[1].append('Avengers')
print(manyList)
print('##########')

for i in manyList:
    if manyList.index(i) != 0:
        i.clear()
print(manyList)