h1, h2 = input().split()
ht = 0
h1 = int(h1)
h2 = int(h2)

if h1 == h2:
    print("O JOGO DUROU 24 HORA(S)")
elif h2 > h1:
    while h2 > h1:
        ht += 1
        h2 -= 1
    print("O JOGO DUROU {} HORA(S)".format(ht))
elif h1 > h2:
    while h1 != h2:
        ht += 1
        h1 += 1
        if h1 == 24:
            h1 = 0
    print("O JOGO DUROU {} HORA(S)".format(ht))