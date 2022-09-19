repetir="s"
alcancia=0
while repetir=="S" or repetir=="s":
    plata=int(input("Ingresar el valora ahorra \n"))
    alcancia=alcancia+plata
    if alcancia<=1000:
        repetir=input("Desea ingresar más dinero S o N para salir \n")
    else:
        print("Rompe la alcancia")
        break
print (f"El total ahorrado es {alcancia}")