def paral(x1, x2, y1, y2):
    d = ((x2-x1)**2+(y2-y1)**2)**0.5
    return d
xA = -3
yA = 11

xB = 12
yB = -4

xC = 1
yC = -7

xD = -14
yD = 8

AB = paral(xA, xB, yA, yB)
CD = paral(xC, xD, yC, yD)

AD = paral(xA, xD, yA, yD)
BC = paral(xB, xC, yB, yC)

if AB==CD and AD==BC:
    print("ABCD - вершины параллелограмма")
else:
    print("ABCD - не являются вершинами параллелограмма")