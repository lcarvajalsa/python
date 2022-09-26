cantidad=int(input("por favor ingrese la cantidad de calificaciones que desea registrar\n"))
suma=0             
for i in range(0, cantidad,1):
    nota=float(input("por favor ingrese su calificación\n"))
    suma=suma+nota
promedio=suma/cantidad
if promedio<3:
    print("tu calificación es", promedio,"Reprobaste\n")
elif promedio<=4 and promedio>=3:
    print ("tu calificación es", promedio,"pasaste raspando\n")
else:
    print ("tu calificación es", promedio,"Aprobaste con buenos resultados\n")
    