lista1=[]
tiempo=[]
menort=60000
registro="s"
while registro=="s" or registro=="S":
    lista1.append (input("Escriba el nombre de jugador\n"))
    registro=(input("Desea registrar otro jugador s para si n para no\n"))
print("Los competidores inscritos son:")
for x in lista1:
    print(x)
print("Tres---\n Dos-----\n Uno-----\n Arranca")
for i in lista1:
    print("Ingese el tiempo en segundos de ", i)
    tiempo.append(int(input()))

for l1, l2 in zip(lista1, tiempo):
    print(l1, l2)
    if l2<menort:
        menort=l2
print (f"Tiempo menor {menort} segundos")
nombre=(tiempo.index(menort))
print (f"Nombre del ganador {lista1[nombre]}\n")

  






