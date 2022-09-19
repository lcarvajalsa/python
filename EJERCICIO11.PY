"Definir un valor inicial del presupuesto ej:100.000"
inicial=1000
"Preguntar al usuario si desea registrar un gasto y capturar el valor"
repetir= input("desea ingresar un valor s para si n para no\n")
gasto=0
gasto_total=0
while repetir=="S" or repetir=="s":
    if inicial>0:
        gasto=int (input("Ingresar un gasto  \n"))
        inicial=inicial-gasto
        gasto_total=gasto_total+gasto
        print("a gastado",gasto,"le queda",inicial,"\n")
        if inicial>0:
            repetir=input("Desea ingresar más dinero S o N para salir \n")
        else:
            print("excediste el gasto\n")  
            break
    else:
        print("excediste el gasto\n")    
        break  
print(f"El total del gasto es {gasto_total}")
print(f"El total del inicial gastado es {inicial}")
