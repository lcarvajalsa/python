total=0
minutos=0
for i in range(1,4,1):
    precio=int(input("Ingrese el precio del producto \n"))
    Cantidad=int(input("Ingrese la cantidad del producto\n"))
    subtotal=precio*Cantidad
    total=total+subtotal
    print(f"valor total {total} pesos colombianos")
    minutos=minutos+1
print("El costo del desayuno es",total)
print(f"por la compra obtuviste {minutos} minutos para recargar e tu movil exito ")
print("Adios")

