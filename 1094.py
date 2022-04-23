N = int(input())

c = 0
r = 0
s = 0

for i in range(N):
    a, b = input().split()
    if b == 'C':
        c = c + int(a)
    if b == 'R':
        r = r + int(a)
    if b == 'S':
        s = s + int(a)
        
total = c+r+s
pc = (c/total)*100
pr = (r/total)*100
ps = (s/total)*100

print("Total: {0} cobaias".format(total))
print("Total de coelhos: {0}".format(c))
print("Total de ratos: {0}".format(r))
print("Total de sapos: {0}".format(s))
print("Percentual de coelhos: {0:.2f} %".format(pc))
print("Percentual de ratos: {0:.2f} %".format(pr))
print("Percentual de sapos: {0:.2f} %".format(ps))