#captura de diez datos 
#te identificas como hombre o mujer
#cuantos hay de hombre o mujeres1
print("te identificas como hombre o mujer \n")
tipo=0
h=0
m=0
for i in range(1,11,1):
    genero=int(input("Ingrese uno para hombre o dos para mujer \n"))
    if genero==1:
        h=h+1
    elif genero==2:
        m=m+1
    else:
        print("no hacer nada")
print(f"hombre {h} mujeres {m}")
