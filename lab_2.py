def lista_osszeg(szamok):
    osszeg = 0
    for szam in szamok:
        osszeg += szam
    return osszeg

def lista_szorzat(szamok):
    szorzat = 1
    for szam in szamok:
        szorzat *= szam
    return szorzat

def billentyuzet_osszeg():
    osszeg = 0
    n = int(input("Add meg a szamot : "))
    for szam in range(n):
        szam = int(input("Add meg a szamot : "))
        osszeg += szam

    return osszeg

def billentyuzet_szorzat():
    szorzat = 1
    n = int(input("Add meg a szamot : "))
    for szam in range(n):
        szam = int(input("Add meg a szamot : "))
        szorzat *= szam
    return szorzat

# print(f"{lista_osszeg([20,40,25,60,21])}")
# print(f"{lista_szorzat([20,40,25,60,21])}")
# print(f"{billentyuzet_osszeg()}")
# print(f"{billentyuzet_szorzat()}")
#print(lista_osszeg([20,40,25,60,21])

def beolvas_billentyuzetrol(n):
    lista = []
    beolvasott_szam = 0
    for i in range(0,n,1):
        beolvasott_szam = int(input("Add meg a szamot : "))
        lista.append(beolvasott_szam)
    return lista


def listabol_legkisebb(lista):
    min_ertek = lista[0]
    poz_list = [0]

    for i in range(1, len(lista), 1):
        if lista[i] < min_ertek:
            min_ertek = lista[i]
            poz_list = [i]
        elif lista[i] == min_ertek:
            poz_list.append(i)

    return min_ertek, poz_list


def billentyuzetrol_legkisebb_pozicio(lista):
    min_ertek = lista[0]
    poz_list = [0]

    for i in range(1, len(lista), 1):
        if lista[i] < min_ertek:
            min_ertek = lista[i]
            poz_list = [i]
        elif lista[i] == min_ertek:
            poz_list.append(i)

    return min_ertek, poz_list

print(f"A listabol megadott legkisebb szam es pozicioja : {listabol_legkisebb([10,10,3,6,7,9])}")
n = int(input("Add meg a lista hosszat : "))
beolvasott_lista = beolvas_billentyuzetrol(n)
print(f"A billentyuzetrol beolvasott lista legkisebb eleme es a pozicioja :  {billentyuzetrol_legkisebb_pozicio(beolvasott_lista)}")
