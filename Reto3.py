#reto3
from random import randint
dado1=randint(1,6)
dado2=randint(1,6)
total=dado1+dado2
print(f"El Dado Rojo cayo {dado1} y Dado Blanco cayo {dado2}")
if dado1==1 and dado2==1:
    print("Si salio pares de unos, Ganaste")
elif dado1==1 and dado2==2 or dado1==2 and dado2==1:
    print("Su total es de tres en los dados, Ganaste")
elif dado1==6 and dado2==5 or dado1==5 and dado2==6:
    print("tu resultado fue 11, Ganaste")
elif dado1==6 and dado2==6:
    print("Ganaste")
elif total==7:
    print("El resultado de su lanzamiento es 7, Ganaste")
else:
    print("Perdiste")