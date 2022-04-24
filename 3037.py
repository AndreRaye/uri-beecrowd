N = int(input())

for i in range(1,N+1):
    Jtotal = 0
    Mtotal = 0
    for i in range(1,4):
        strJx, strJd = input().split()
        Jx = int(strJx)
        Jd = int(strJd)
        soma1 = Jx*Jd
        Jtotal = Jtotal + soma1
        
    for i in range(1,4):
        strMx, strMd = input().split()
        Mx = int(strMx)
        Md = int(strMd)
        soma2 = Mx*Md
        Mtotal = Mtotal + soma2

    if Jtotal > Mtotal:
        vencedor = 'JOAO'
    if Mtotal > Jtotal:
        vencedor = 'MARIA'
    
    print(vencedor)