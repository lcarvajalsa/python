"En la materia de programacion con python tenemos 4 talleres a desarrollar y"
"queremos determinar si su aprendiz aprobó o reprobo la materia:"
"Solicita la nota optenida en cada uno de los 4 talleres calificacion de 1.0 a 5.0."
num1=float(input("Ingrese primer taller\n "))
num2=float(input("Ingrese segundo taller\n "))
num3=float(input("Ingrese tercer taller\n "))
num4=float(input("Ingrese cuarto taller\n "))
total=(num1+num2+num3+num4)/4
print("La suma entre",num1,"y",num2, "y",num3,"y",num4,"es",total)
"Calcular la nota final de la materia teniendo en cuenta que se promedian las 4"
"notas de los talleres."
"Mostrar un mensaje en pantalla de acuerdo a la nota final obtenida, si:"
if 0.0<=total <=2.9:
    print("reprobaste la asignatura")
elif 3.0<=total <=3.9:
    print("pasaste raspando la asignatura")
else:
    print("Aprobaste la asignatura")

