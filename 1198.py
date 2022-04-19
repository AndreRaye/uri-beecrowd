while True:
    try:
        soldados = input()
    except EOFError:
        break

    strsH, strsI = soldados.split()
        
    sH = int(strsH)
    sI = int(strsI)

    print(abs(sH - sI))