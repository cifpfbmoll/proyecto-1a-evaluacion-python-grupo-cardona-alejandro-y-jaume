def sacarcarta (lista):

    carta=lista.pop(0)

    return carta

def barajar (lista):

    import random

    random.shuffle(lista)

    return lista

def nombrejugadores (numerojugadores):

    listajugadores=[]

    for i in range(1,numerojugadores+1):

        nombrejugador=str(input(f" > Escribe el nombre del {i} jugador:"))

        listajugadores.append([nombrejugador])

    return listajugadores

def dinerojugadores (listajugadores):

    for i in range (len(listajugadores)):

        dinero=int(input(f" > Introducir dinero de {listajugadores[i][0]}:"))

        listajugadores[i].append(dinero)

    return listajugadores

def apuestajugadores (listajugadores):

    for i in range (len(listajugadores)):

        apuesta=int(input(f" > Introducir apuesta de {listajugadores[i][0]}:"))

        listajugadores[i].append(apuesta)

    return listajugadores