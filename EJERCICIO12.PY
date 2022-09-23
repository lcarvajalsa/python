#Realice la creación de una lista llamada baul
baul=[]
#Cree mediante una estructura cíclica un mecanismo para solicitar a
#las siguientes opciones a un jugador
seguir="s"
#Agregar un artículo al baúl a voluntad (se agrega al final de la lista)
#Ej: espada, casco, etc
while seguir=="s" or seguir=="S":
    print("seleccione:\n 1 Agregar un artículo al baúl a voluntad\n 2 Listar artículos del baúl de forma ascendente \n 3 Borrar el último elemento de la lista\n 4 Borrar un artículo del bául\n")
#Agregar un artículo al baúl a voluntad
    de=int(input("Que opcion desea elegir\n"))
    if de==1: 
        baul.append(input("Agregar un artículo\n"))
#Listar artículos del baúl de forma ascendente
    elif de==2:
            print("esto son lo elementos\n")
            baul.sort()
            print(baul)
#Borrar el último elemento de la lista
    elif de==3:
        print("vas a eliminar el último elemento de la lista\n")
        baul.pop()
        print(baul)
#Borrar un artículo del bául
    elif de==4:
        for index,articulo in enumerate(baul):
            print(index, articulo)
            print(f"#{index} => {articulo}")
            del baul[int(input("ingrese el numero del articulo que desea borrar\n"))]
            print("haz eliminado con exito el articulo solicitado\n")
    else:
        print("opcion incorrecta\n")
    seguir=input("deseas ingresar al menu s o n para terminar\n")      

#debe mostrarlos con su index y permitir
#escoger a un usuario cual desea borrar.