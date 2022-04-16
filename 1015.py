from math import sqrt

strx1, stry1 = input().split()
strx2, stry2 = input().split()

x1 = float(strx1)
x2 = float(strx2)
y1 = float(stry1)
y2 = float(stry2)

d = sqrt((x2-x1)**2 + (y2-y1)**2)

print(("{0:.4f}".format(d)))