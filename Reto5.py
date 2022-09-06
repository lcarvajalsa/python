#En Supermercados Noé estamos de aniversario y 
# te obsequiamos un descuento en el valor de tu compra, 
# si ésta es mayor a 50.000 y dependiendo de tu suerte:
#Si sacas la bolita roja obtienes 10% en el valor de tu compra
from random import randint, random

bolita=randint(1,4)

print("Bienvenido a supermercados Noé\n")
total=int(input("Ingrese el valor a pagar \n"))
if total>=50000:
    print("Tu compra supera los 50000 pesos colombianos\n")
    print("y te obsequiamos un descuento en el valor a pagar\n")
    print("Si sacas la bolita roja obtienes descuento del 10%\n") 
    print("Si sacas la bolita azul obtienes descuento del 30%\n")
    print("Si sacas la bolita amarilla obtienes descuento del 50%\n")
    print("Si sacas la bolita blanca te llevas tu compra total mente Gratis\n")
    if bolita==1:
        total=total-((total*10)/100)
        print("sacaste la Roja")
        print("tu valor a pagar es ",total,)
    elif bolita==2:
        total=total-((total*30)/100)
        print("sacaste la Azul")
        print("tu valor a pagar es ",total)
    elif bolita==3:
        total=total-((total*50)/100)
        print("sacaste la Amarilla")
        print("tu valor a pagar es ",total)
    elif bolita==4:
        print("llevas tu compra gratis Ganaste....")
else:
     print("Su valor a pagar es",total, "pesos colombianos\n")




