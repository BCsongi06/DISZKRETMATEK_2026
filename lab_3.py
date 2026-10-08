#5
import sys


def olvasas(filename = "szamok.txt"):
    with open(filename) as f:
        sorok = f.readlines()
    szamok = []
    for s in sorok:
        #print(s)
        a,b = s.split()
        a,b = int(a),int(b)
        szamok.append((a,b))
        #print(a,b)
    return szamok
    #print(sorok)


# szamok = olvasas()
# print(szamok)

def myEuklidesz(a,b):
    while b!=0 :
        maradek = a%b
        a = b
        b = maradek

    return a

def lnko_kivonas(a,b):
    while a!=b:
        if a>b:
            a = a-b
        else : b = b - a

    return a

import math

def main():
    szamok = olvasas()
    for (a,b) in szamok:
        lnko1 = lnko_kivonas(a,b)
        lnko2 = myEuklidesz(a,b)
        lnko3 = math.gcd(a,b)
        lkkt = (a*b) // lnko1
        print(f"{lnko1} {lnko2} {lnko3} ,lkkt: {lkkt}")

if __name__ == "__main__":
    main()



