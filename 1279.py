linha = 0

while True:
    try:
        ano = int(input())
        ordinary = 1
        bi = 0

        if ano < 2000:
            ano = int(input())
        
        if linha:
            print("")
        linha = 1

        if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
            ordinary = 0
            bi = 1
            print("This is leap year.")
        if ano % 15 == 0:
            ordinary = 0
            print("This is huluculu festival year.")
        if ano % 55 == 0 and bi:
            ordinary = 0
            print("This is bulukulu festival year.")
        if ordinary:
            print("This is an ordinary year.")

    except EOFError:
        break