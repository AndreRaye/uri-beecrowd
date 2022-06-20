resultado = [["empate", "sheldon", "rajesh", "rajesh", "sheldon"],\
             ["rajesh", "empate", "sheldon", "sheldon", "rajesh"],\
             ["sheldon", "rajesh", "empate", "rajesh", "sheldon"],\
             ["sheldon", "rajesh", "sheldon", "empate", "rajesh"],\
             ["rajesh", "sheldon", "rajesh", "sheldon", "empate"]]

def pos(jogada):
    if jogada == "pedra":
        return 0
    elif jogada == "papel":
        return 1
    elif jogada == "tesoura":
        return 2
    elif jogada == "lagarto":
        return 3
    else:
        return 4
    
n = int(input())

for i in range(n):
    Rajesh, Sheldon = input().split()
    print(resultado[pos(Rajesh)][pos(Sheldon)])