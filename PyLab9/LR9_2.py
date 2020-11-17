import numpy

array = numpy.array([1,5,5,2,8,2,3,5,6,8,1,2,1])
currentMax = array[0]
currentMaxIndex = 0

for i in range(len(array)):
    if (array[i] > currentMax):
        currentMax = array[i]
        currentMaxIndex = i

array[currentMaxIndex] = 0
print(array)