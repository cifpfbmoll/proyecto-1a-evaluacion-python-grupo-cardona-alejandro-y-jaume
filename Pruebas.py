

lista=["jugador","sudinero",["apuesta"],["cartasenMano"],"valormano"]

apuesta=lista[2][0]

doblar=apuesta+apuesta

lista.pop([2][0])

lista.insert(2,[doblar])

print(lista)