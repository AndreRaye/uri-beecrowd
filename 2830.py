K = int(input())

while K < 1 or K > 16:
    K= int(input())

L = int(input())

while L < 1 or L > 16 or L == K:
    L = int(input())

if ((L-1)//2 == (K-1)//2):
    print("oitavas")
elif ((L-1)//4 == (K-1)//4):
    print("quartas")
elif ((L-1)//8 == (K-1)//8):
    print("semifinal")
else:
    print("final")