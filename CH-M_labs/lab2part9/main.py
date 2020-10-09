fio = 'Azarenkov Artur Alekseevich'
print(len(fio))
fioList = fio.split(' ')
print(fioList)
print(fio.count('o'))
print(fio.count('e'))

fio_S = fioList[0] + '\n' + fioList[1] + '\t' + fioList[2]
print(fio_S)
print(len(fio_S))