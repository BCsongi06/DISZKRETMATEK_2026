import math

def osszeg(x, y):
    return x + y

def kulonbseg(x, y):
    return x - y

def szorzat(x, y):
    return x * y

def hanyados(x, y):
    if y != 0:
        return x / y
    return 0

def maradek(x, y):
    if y != 0:
        return x % y
    return 0

def maximum(x, y):
    if x > y:
        return x
    return y

def minimum(x, y):
    if x < y:
        return x
    return y

def elsofoku_gyok(a, b):
    if a != 0:
        return -b / a
    return None

def abszolut(x):
    if x < 0:
        return -x
    return x

def elojel(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    return 0

def also_egesz(x):
    return math.floor(x)

def felso_egesz(x):
    return math.ceil(x)

def masodfoku_gyok(a, b, c):
    d = b**2 - 4*a*c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        return -b / (2*a)
    return None

def byte_szukseglet():
    k = int(input("k = "))
    return math.ceil(k / 8)

def elso_n_termeszetes(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(i)
    return lista

def elso_n_paros(n):
    lista = []
    for i in range(2, n + 1, 2):
        lista.append(i)
    return lista

def n_darab_paros(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(2 * i)
    return lista

def elso_n_paratlan(n):
    lista = []
    for i in range(1, n + 1, 2):
        lista.append(i)
    return lista

def n_darab_paratlan(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(2 * i - 1)
    return lista

def elso_n_negyzetszam(n):
    lista = []
    for i in range(1, int(math.sqrt(n)) + 1):
        lista.append(i**2)
    return lista

def n_darab_negyzetszam(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(i**2)
    return lista

def elso_n_osszeg(n):
    o = 0
    for i in range(1, n + 1):
        o += i
    return o

def elso_n_szorzat(n):
    sz = 1
    for i in range(1, n + 1):
        sz *= i
    return sz

def ketto_hatvanyai(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(2**i)
    return lista

def x_hatvanyai(n):
    x = int(input("x = "))
    lista = []
    for i in range(1, n + 1):
        lista.append(x**i)
    return lista

def negyzetgyokok(szamok):
    lista = []
    for sz in szamok:
        if sz >= 0:
            lista.append(math.sqrt(sz))
    return lista

def legnagyobb_elem(szamok):
    max_szam = szamok[0]
    for sz in szamok:
        if sz > max_szam:
            max_szam = sz
    return max_szam

def legnagyobb_sorszama(szamok):
    max_szam = szamok[0]
    index = 0
    for i in range(len(szamok)):
        if szamok[i] > max_szam:
            max_szam = szamok[i]
            index = i
    return index + 1

def szamok_osszege(szamok):
    o = 0
    for sz in szamok:
        o += sz
    return o

def szamok_szorzata(szamok):
    sz = 1
    for s in szamok:
        sz *= s
    return sz

def nullak_faktorialis_vegen(n):
    nullak = 0
    while n >= 5:
        n //= 5
        nullak += n
    return nullak