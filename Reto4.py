from random import randint, random
print("Bueno vamos a jugar")
jugar=randint(1,3)
eleccion=int(input( "Digite 1 para piedra y 2 para papel o 3 para tijera \n"))
if jugar==1 and eleccion==1:
    print(" Salio Piedra, usted eliguio piedra sigue participando....")
elif jugar==1 and eleccion==2:
    print(" Salio Piedra, usted eliguio papel Ganaste....")
elif jugar==1 and eleccion==3:
    print(" Salio piedra, usted eliguio tijera Perdiste....")
elif jugar==2 and eleccion==1:
    print(" Salio papel, usted eliguio piedra perdiste....")
elif jugar==2 and eleccion==2:
    print(" Salio papel, usted eliguio papel sigue participando....")
elif jugar==2 and eleccion==3:
    print(" Salio papel, usted eliguio tijera Ganaste....")
elif jugar==3 and eleccion==1:
    print(" Salio tijera, usted eliguio piedra Perdiaste....")
elif jugar==3 and eleccion==2:
    print(" Salio tijera, usted eliguio papel perdiste....")
elif jugar==3 and eleccion==3:
    print(" Salio tijera, usted eliguio tijera sigue participando....")
else:
    print("sigue intentando")




