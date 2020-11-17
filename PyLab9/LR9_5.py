import numpy

isSymmetric = True
array = numpy.array([numpy.array([0,3,1,4]),
                     numpy.array([3,0,1,4]),
                     numpy.array([1,1,0,1]),
                     numpy.array([4,4,1,0])])

for i in array:
    print(i)

for i in range(len(array)):
    for j in range(len(array[i])):
        if (array[i][j] != array[j][i] and i != j):
            isSymmetric = False

print("Result:", isSymmetric)