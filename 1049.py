A = input()
B = input()
C = input()

v = 0
i = 0
a = 0
m = 0
ii = 0
an = 0
c = 0
o = 0
h = 0
he = 0


if A == 'vertebrado':
    v = 1
if A == 'invertebrado':
    i = 1

if B == 'ave':
    a = 1
if B == 'mamifero':
    m = 1
if B == 'inseto':
    ii = 1
if B == 'anelideo':
    an = 1

if C == 'carnivoro':
    c = 1
if C == 'onivoro':
    o = 1
if C == 'herbivoro':
    h = 1
if C == 'hematofago':
    he = 1

if v and a and c:
    print("aguia")
if v and a and o:
    print("pomba")
if v and m and o:
    print("homem")
if v and m and h:
    print("vaca")
    
if i and ii and he:
    print("pulga")
if i and ii and h:
    print("lagarta")
if i and an and he:
    print("sanguessuga")
if i and an and o:
    print("minhoca")