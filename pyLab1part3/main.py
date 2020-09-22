import numpy

a1 = 1.0
b1 = 2.5
c1 = 3.0
a2 = 4.9
b2 = 5.0
c2 = 6.0
A = [[a1, b1], [a2, b2]]
B = [[a1, b1], [a2, b2], [c1, c2]]
freeMembersVector = [c1, c2]
rA = numpy.linalg.matrix_rank(A)
rB = numpy.linalg.matrix_rank(B)
if rA == rB:
    if rA == 2:
        M1 = numpy.array([[a1, b1], [a2, b2]])
        v1 = numpy.array([c1, c2])
        print(numpy.linalg.solve(M1, v1))
    else:
        print("infinity")
else:
    print("No solution")
