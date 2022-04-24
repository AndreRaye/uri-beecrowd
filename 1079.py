N = int(input())

for i in range(1,N+1):
    strA,strB,strC = input().split()
    A = float(strA)
    B = float(strB)
    C = float(strC)
    A = A*2
    B = B*3
    C = C*5
    media = (A+B+C)/10
    print("{0:.1f}".format(media))