workerList = []
f = open("2.txt", 'r')
workers = 0 # количество работников
for i in f:
    workers += 1
f.close()
f = open("2.txt", 'r')
for i in range(workers):
    workerList.append(f.read(27))

# a
print("1. Doctors with more than 5 years of working:\n")
for worker in workerList:
    if worker[0:6] == "doctor" and int(worker[7:9]) >= 5:
        print(worker)

# b
print("2. Economists with higher education younger 35:\n")
for worker in workerList:
    if worker[0:6] == "econom" and worker[10:16] == "higher" and int(worker[24:26]) <= 35:
        print(worker)

#c
print("3. Economists with trading experience:\n")
for worker in workerList:
    if worker[0:6] == "tradin" and int(worker[7:9]) >= 0:
        print(worker)

#d
print("4. Females at age 20-40:\n")
for worker in workerList:
    if worker[17:23] == "female" and int(worker[24:26]) >= 20 and int(worker[24:26]) <= 40:
        print(worker)

#e
print("5. Average age of males:\n")
ageSum = 0
malesNum = 0
for worker in workerList:
    if worker[17:23] == "__male":
        malesNum += 1
        ageSum += int(worker[24:26])
print(ageSum/malesNum, "\n")

#f
print("6. With higher education more:\n")
maleEduNum = 0
femaleEduNum = 0
for worker in workerList:
    if worker[17:23] == "__male" and worker[10:16] == "higher":
        maleEduNum += 1
    if worker[17:23] == "female" and worker[10:16] == "higher":
        femaleEduNum += 1
if malesNum > femaleEduNum:
    print("male\n")
else:
    print("female\n")

#g
print("7. Enter N (for most young workers):\n")
# ввести сколько самых молодых работников хотим получить
n = int(input())
youngList = []
for worker in workerList:
    youngList.append(int(worker[24:26]))
youngList.sort()
youngEdge = youngList[n]
for worker in workerList:
    if int(worker[24:26]) < youngEdge:
        print(worker)