from random import randint, random
total=0
apostar=1000
valor=0
repetir=int(input("Digite las veses que decea jugas\n"))
valor=int(input("Digite cuanto vas a apostar\n"))
seguir=input
for i in range(1,repetir,1):
    while repetir==repetir or repetir==repetir:
        if valor>0:
            moneda=randint(1,2)
            eleccion=int(input( "Digite 1 para cara y 2 para cello \n"))
            if moneda==1 and eleccion==1:
                print(" Salio cara, usted eliguio cara Ganaste....")
            elif moneda==1 and eleccion==2:
                print(" Salio cara, usted eliguio sello Perdiste....")
            elif moneda==2 and eleccion==2:
                print(" Salio sello, usted eliguio sello Ganaste....")
            elif moneda==2 and eleccion==1:
                print(" Salio sello, usted eliguio cara perdiste....")
            elif eleccion!=1 or eleccion!=2:
                print("Digitaste una opcion incorrecta")
            else:
                print("sigue intentando")
            if apostar<1000:
                repetir=input("Desea ingresar más dinero S o N para salir \n")
            else:
                print("excediste el gasto\n")  
                break
        else:
            print("excediste el gasto\n")    
            break  
    total=total+valor
    apostar=apostar-valor
    print(f"El total del gasto es {apostar}")
    print(f"tienes un saldo de {total}")




        