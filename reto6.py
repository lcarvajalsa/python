from random import randint
election=int(input("Digita 1 para el valor de su factura o 2 para la cantidad de productos \n"))
if election==1:
    compra=int(input("Ingrese el valor de su compra \n"))
else:
    numproductos=int(input("Ingrese el numero de productos a comprar\n "))
    valorproducto=10000
    compra=numproductos*valorproducto  
descuento=randint(1,4)
total=compra
if compra>50000:
    print("Salio seleccionado para participar en nuestra promocion de aniversario\n")
    if descuento==1:
        procedimiento=compra*0.10
        total=compra-procedimiento
        print("Salio bolita roja, su descuento es del 10% en el valor de su factura, su total a pagar es",total,"\n")
    elif descuento==2:
        procedimiento=compra*0.30
        total=compra-procedimiento
        print("Salio bolita azul, su descuento es de 30% en el valor de su factura,su total a pagar es",total, "\n")
    elif descuento==3:
        procedimiento=compra*0.50
        total=compra-procedimiento
        print("Salio bolita amarilla, su descuento es de 50% en el valor de su factura,su total a pagar es ",total,"\n")
    elif descuento==4:
        print("Salio bolita blanca, te llevas tu compra gratis\n")
    else:
        print(f"El juego escogio{descuento}")
else:
    print("Su total a pagar es ",compra,"\n")
    valorrecibido1=int(input("Igrese el valor con el que desea cancelar\n "))
    cambio=valorrecibido1-compra
    print ("Su compra fue de ",compra," productos me realizo el pago con ",valorrecibido1," su cambio es ",cambio,"\n")
if descuento==1 or descuento==2 or descuento==3:
    valorrecibido=int(input("igrese el valor con el que desea cancelar\n "))
    cambio=valorrecibido-total
    print ("Su compra fue de ",total," productos me realizo el pago con ",valorrecibido," su cambio es ",cambio,"\n")
else: 
    descuento==4
    print("----Gracias por su compra----")