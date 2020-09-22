def Square(x1, y1, x2, y2, x3, y3):
    return abs(1/2 * ((x1-x3)*(y2-y3) - (y1-y3)*(x2-x3)))

aX = 0.
aY = 2.
bX = 2.
bY = 0.
cX = 0.
cY = 0.
dX = 1.
dY = 1.

ABCSquare = Square(aX, aY, bX, bY, cX, cY)
ABDSquare = Square(aX, aY, bX, bY, dX, dY)
BCDSquare = Square(bX, bY, cX, cY, dX, dY)
CADSquare = Square(cX, cY, aX, aY, dX, dY)
Sum = ABDSquare + BCDSquare + CADSquare

if (ABCSquare < Sum):
     print("no")
else:
     print("yes")
