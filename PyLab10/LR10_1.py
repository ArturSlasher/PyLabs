def lessMax(array):
    currentMax = 0
    currentLessMax = 0

    for i in range(len(array)):
        if (array[i] >= currentMax):
            currentMax = array[i]

    for j in range(len(array)):
        if (array[j] >= currentLessMax and array[j] != currentMax):
            currentLessMax = array[j]
    return currentLessMax

array = [4,5,7,89,1,3,45,2,89,17,0,9]
print(lessMax(array))
