#hacer un programa de algo cotidiano
from re import S
print("si tu cuenta de correo es MISENA marca 1 o 2 si es personal")
num1=int(input("Ingrese el primer número\n "))
while num1==2:
    rta1=input("¿Registrarse en el sena? S para si, N para no \n" )
    if rta1=="S" or rta1=="s":
        print("Ahora tienes un coreo MISENA \n")
        num1=1
    else:
        break
if num1==1:
            print("Tu correo es misena")
            rta=input("¿Es correcto? escribe si de lo contrario no \n")
            if rta=="si" :
                print("Eres aprendiz del SENA")
            elif rta=="Si":
                print("Eres aprendiz del SENA")
            elif rta=="SI":
                print("Eres aprendiz del SENA")
            elif rta=="sI":
                print("Eres aprendiz del SENA")
            else:
                print("No se te olvide activar tu cuenta soysena")
            materias=int(input("Cuantas materias quieres inscribir: \n"))
            for i in range(0,materias,1):
                print ("Materia inscrita satisfactoriamente \n")
            print("Tienes",materias," incritas")
            repetir="s"
            diario=0
            while repetir=="S" or repetir=="s":
                plata=int(input("Ingresa tus gastos unitarios del dia \n"))
                diario=diario+plata
                if diario<=10000:
                    repetir=input("Desea ingresar más gastos S o N para salir \n")
                else:
                    print("Te quedaste sin plata retira por nequi")
                    break
            print=input(f"Solo sacase 10000 y te estas gastando {diario}")
        
else:
    print("Tienes la oportunidad de ser parte del SENA")








