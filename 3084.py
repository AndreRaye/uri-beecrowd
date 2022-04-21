while True:
    try:
        horarios = input()
    except EOFError:
        break

    strH, strM = horarios.split()

    h = int(strH)
    m = int(strM)

    h = h/30
    m = m/6

    h = int(h)
    m = int(m)

    print("{0:02d}:{1:02d}".format(h,m))
