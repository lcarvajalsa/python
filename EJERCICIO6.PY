print("piensa un numero")
print("suna 5")
print("multiplica 3")
print("reste 15")
res=int(input("Digita el número que te dió \n"))
num=res/3
print(f"El número que pensaste.....\n es .....\n {int(num)} ")
rta=input("¿Es correcto? escribe si de lo contrario no")
if rta=="si" or rta=="Si" or rta=="SI" or rta=="sI" :
    print("Soy todo un adivino")
else:
    print("Rectifica las cuentas te darás cuenta que no me equivoco")