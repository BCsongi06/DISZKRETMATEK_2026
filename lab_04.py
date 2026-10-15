# #szulinapos feladat
# # import random
# # def van_utkozes(n,M):
# #     szulinapok = []
# #     for _ in range(n):
# #         nap = random.randint(1, M)
# #         if nap in szulinapok:
# #             return True
# #         szulinapok.append(nap)
# #     return False
# #
# # K = 100_000
# # db = 0
# # for _ in range(K):
# #     if van_utkozes(7,30):
# #         db += 1
# # print(db / K)
# import sympy
# #a,b,c = 19,59,1709
# #a,b,c = 200,500,5100
# a, b = 14, 21
# c_lista = [350, 400, 777]
# xk,yk,d = sympy.gcdex(a,b)
# #print(f"ellenorzes: {a}*{x}+{b}*{y} = {d}, {a*x+b*y==d}")
#
#
# #3.7
# from sympy import gcdex
# import math
# for c in  c_lista:
#     x = (xk*c)//d
#     y = (yk*c)//d
#     t1 = int(math.ceil((-x*d) /b))
#     t2 = int(math.floor((y*d)/a))
#     print(f"t1 = {t1}, t2 = {t2}")
#     #maxi = 0
#     for n in range(t1,t2+1):
#         x1 = x+(n*b)//d
#         y1 = y-(n*a)//d
#         #if maxi < x1+y1 :
#             #maxi = x1+y1
#         print(x1,y1,"teszt = ", x1*a+y1*b==c)
#     #print(f"maximum = {maxi}")
#
#
# #9
def myPowLog(alap,kitevo):
    res =1
    while kitevo != 0 :
        kitevo = kitevo //2
        if kitevo == 0 : break
        alap = (alap * alap)
    return res


import math

def beolvas_billentyuzetrol():
    temp = input("x y n :")
    x, y, n = temp.split(" ")
    x, y, n = int(x), int(y), int(n)
    x = x// math.gcd(x,y)
    y = y//math.gcd(x,y)
    print(f"irreducibilis alak : {x}/{y}")
    eredmeny1 = myPowLog(x,n)
    eredmeny2 = myPowLog(y,n)
    print(eredmeny1,"/",eredmeny2)

beolvas_billentyuzetrol()
