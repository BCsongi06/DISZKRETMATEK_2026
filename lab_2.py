# def lista_osszeg(szamok):
#     osszeg = 0
#     for szam in szamok:
#         osszeg += szam
#     return osszeg
#
# def lista_szorzat(szamok):
#     szorzat = 1
#     for szam in szamok:
#         szorzat *= szam
#     return szorzat
#
# def billentyuzet_osszeg():
#     osszeg = 0
#     n = int(input("Add meg a szamot : "))
#     for szam in range(n):
#         szam = int(input("Add meg a szamot : "))
#         osszeg += szam
#
#     return osszeg
#
# def billentyuzet_szorzat():
#     szorzat = 1
#     n = int(input("Add meg a szamot : "))
#     for szam in range(n):
#         szam = int(input("Add meg a szamot : "))
#         szorzat *= szam
#     return szorzat
#
# # print(f"{lista_osszeg([20,40,25,60,21])}")
# # print(f"{lista_szorzat([20,40,25,60,21])}")
# # print(f"{billentyuzet_osszeg()}")
# # print(f"{billentyuzet_szorzat()}")
# #print(lista_osszeg([20,40,25,60,21])
#
# def beolvas_billentyuzetrol(n):
#     lista = []
#     beolvasott_szam = 0
#     for i in range(0,n,1):
#         beolvasott_szam = int(input("Add meg a szamot : "))
#         lista.append(beolvasott_szam)
#     return lista
#
#
# def listabol_legkisebb(lista):
#     min_ertek = lista[0]
#     poz_list = [0]
#
#     for i in range(1, len(lista), 1):
#         if lista[i] < min_ertek:
#             min_ertek = lista[i]
#             poz_list = [i]
#         elif lista[i] == min_ertek:
#             poz_list.append(i)
#
#     return min_ertek, poz_list
#
#
# def billentyuzetrol_legkisebb_pozicio(lista):
#     min_ertek = lista[0]
#     poz_list = [0]
#
#     for i in range(1, len(lista), 1):
#         if lista[i] < min_ertek:
#             min_ertek = lista[i]
#             poz_list = [i]
#         elif lista[i] == min_ertek:
#             poz_list.append(i)
#
#     return min_ertek, poz_list
#
# print(f"A listabol megadott legkisebb szam es pozicioja : {listabol_legkisebb([10,10,3,6,7,9])}")
# n = int(input("Add meg a lista hosszat : "))
# beolvasott_lista = beolvas_billentyuzetrol(n)
# print(f"A billentyuzetrol beolvasott lista legkisebb eleme es a pozicioja :  {billentyuzetrol_legkisebb_pozicio(beolvasott_lista)}")

#gyorshatvanyozas
#3

# def myPowRec(x, n):
#     if n == 0: return 1
#     temp = myPowRec(x, n // 2)
#     if n % 2 == 0:
#         return temp * temp
#     return temp * temp * x
#
# def myPowIt(x, n):
#     if n == 0: return 1
#     res = 1
#     while n > 0:
#         if n & 1 == 1:
#             res *= x
#         n //= 2
#         if n > 0:
#             x *= x
#     return res
#
# def myPowItCount(x, n):
#     if n == 0: return 1
#     res, count = 1, 0
#     while n > 0:
#         if n & 1 == 1:
#             res *= x
#             count += 1
#         n //= 2
#         if n > 0:
#             x *= x
#             count += 1
#     return count, res
#
# def myPowMod(x, n, m):
#     if n == 0:
#         return 1
#     res = 1
#     while n > 0:
#         if n & 1 == 1:
#             res = (res * x) % m
#         n //= 2
#         if n > 0:
#             x = (x * x) % m
#     return res
#
# print(myPowRec(2, 10))
# print(myPowIt(2, 1000))
# print(myPowItCount(2, 10))
#
# for n in [10, 50, 100, 500, 1000, 1500, 2000, 10000]:
#     count, res = myPowItCount(2, n)
#     print(f"2^{n} - {count} szorzás")
#
# print(myPowMod(2, 1000, 23))
# print(pow(2, 1000, 23))
# print(pow(2, 1000) % 23)

#6

def kobLista(n):
    lista = [x * x * x for x in range( n + 1)]
    #lista =[x ** 3 for x in [2,500,-3,4]]
    return lista

def kettoHatvLista(n):
    lista = [(x,2**x) for x in range( n + 1)]
    return lista

def haromHatvLista(n):
    lista = [(x,3**x) for x in range( n + 1)]
    return lista

def altalanosLista(a,n):
    lista = [(x,a**x) for x in range( n + 1)]
    return lista

def duplaciklus(n):
    db = 0
    for i in range(n+1):
        for j in range(i):
            if db == n:
                break
            print(i, end='')
            db +=1
        if db == n:
            break

def duplaciklusListaval(n):
    db = 0
    lista = []
    for i in range(n+1):
        for j in range(i):
            if db == n:
                break
            lista.append(i)
            db +=1
            if db ==n:
                break

    return lista

def sorozat(n):
    db = 0
    lista = []
    for i in range(1, n + 1):
        ertek = 1 if i % 2 == 1 else 0
        for j in range((i + 1) // 2):
            lista.append(ertek)
            db += 1
            if db == n:
                break
        if db == n:
            break
    return lista

def duplaciklusParListaval(n):
    db = 0
    lista = []
    for i in range(1, n + 1):
        ismetles = 1
        if i & 1 == 0:
            ismetles = 2
        for j in range(ismetles):
            if db == n:
                break
            lista.append(i)
            db += 1
        if db == n:
            break

    return lista
# print(kobLista(5))
# print(kettoHatvLista(5))
# print(haromHatvLista(5))
# print(altalanosLista(4,5))
duplaciklus(10)
print(duplaciklusListaval(10))
print(sorozat(10))
print(duplaciklusListaval(10))
