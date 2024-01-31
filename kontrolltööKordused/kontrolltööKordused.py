#1
for n in range(0,10,1):
    n=""" ^---^
( o o )
! = !/)

"""
    print (f"{n:7}", end=" ")
    print()


# #2
n=int(input("valige number:"))
aste=int(input("millisel määral:"))
vastus=n ** aste
if vastus<n*100:
    print(vastus)
else:
    print("liiga suur number")


#3
import random
õpite = 25
klassid = [random.randint(1, 5) for _ in range(õpite)]  #alajaotust on vaja selleks, et vältida muutuja kasutamist tsükli sees.
min_otsus = max_otsus = klassid[0]
for otsus in klassid[1:]: #mis tähendab, et kõiki hindeid kontrollitakse ükshaaval, alustades esimesest.
    min_otsus = otsus if otsus < min_otsus else min_otsus
    max_otsus = otsus if otsus > max_otsus else max_otsus
    
print ("kõik klassid", klassid)
print("minimaalne", min_otsus)
print("maksimaalne", max_otsus)

# 4
ameba=1
interval=3
for i in range(3,25,3):
    osakond=ameba * 2 ** (i // interval)
    print("läbi", i, "tund on", osakond, "amoeba")
