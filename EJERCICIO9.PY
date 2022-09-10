total=0
#Contador debe iniciar en cero antes del ciclo
minutos=0
for i in range(1,4,1):
    precio=int(input("Ingrese el precion del producto \n"))
    Cantidad=int(input("Ingrese la cantidad del producto\n"))
    subtotal=precio*Cantidad
    total=total+subtotal
    print(f"valor total {total} pesos colombianos")
    #COntador vive dentro de un ciclo pero aunemta en un valor fijo
    minutos=minutos+1
    #minutos+=1 abreviada
print("El costo del desayuno es",total)
print(f"por la compra obtuviste {minutos} minutos para recargar e tu movil exito ")
print("Adios")

