N = int(input())

vet_int = [0]*N

vet_int = input().split()

for i in range(N):
    vet_int[i] = int(vet_int[i])
    
min_int = vet_int[0]
pos = 0

for i in range(1, N):
    if vet_int[i] < min_int:
        min_int = vet_int[i]
        pos = i
        
print("Menor valor:", min_int)
print("Posicao:", pos)
        