#hacer un programa de algo cotidiano
print("si tu cuenta de correo es gmail parca 1 o 2 si es misena")
num1=int(input("Ingrese el primer número\n "))
if num1==1:
    print("tienes la oportunidad de ser parte del SENA")
else:
    print("tu correo es misena")
rta=input("¿Es correcto? escribe si de lo contrario no \n")
if rta=="si" :
    print("eres aprendiz del SENA")
elif rta=="Si":
    print("eres aprendiz del SENA")
elif rta=="SI":
    print("eres aprendiz del SENA")
elif rta=="sI":
    print("eres aprendiz del SENA")
else:
    print("no se te olvide activar tu cuenta soysena")
for i in range(1,3,1):
    num=int(input("confirma tus clases principales 1 paython 2 bases de datos \n"))
repetir="s"
diario=0
while repetir=="S" or repetir=="s":
    plata=int(input("Ingresa tus gartos unitarios del dia \n"))
    diario=diario+plata
    if diario<=10000:
        repetir=input("Desea ingresar más gastos S o N para salir \n")
    else:
        print("te quedaste sin plata retira por nequi")
        break
print=input(f"Solo sacase 10000 y te estas gastando {diario}")








