def sacarcarta (lista):

    carta=lista.pop(0)

    return carta

def barajar (lista):

    import random

    lista=random.shuffle(lista)

    return lista

def nombrejugadores (numerojugadores):

    listajugadores=[]

    for i in range(1,numerojugadores+1):

        nombrejugador=str(input(f"Escribe el nombre del {i} jugador:"))

        listajugadores.append([nombrejugador])

    return listajugadores

def dinerojugadores (listajugadores):

    for i in range (len(listajugadores)):

        dinero=int(input(f"{listajugadores[i][0]}:"))

        listajugadores[i].append(dinero)

    return listajugadores