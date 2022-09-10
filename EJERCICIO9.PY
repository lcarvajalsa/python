total=0

for i in range(1,4,1):
    precio=int(input("Ingrase el precion del producto \n"))
    Cantidad=int(input("Ingrese la cantidad del producto\n"))
    subtotal=precio*Cantidad
    total=total+subtotal
    print(f"valor total",total, "pesos colombianos")
print("Adios")
