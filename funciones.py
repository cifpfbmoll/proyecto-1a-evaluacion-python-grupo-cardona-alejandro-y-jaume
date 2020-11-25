
def sacarcarta (lista):

    carta=lista.pop(0)

    return carta

def repartircartasiniciales (listajugadores,baraja):

    for i in range (len(listajugadores)):

        if listajugadores[i][-1]==listajugadores[i][2]:
        
            carta=sacarcarta(baraja)

            listajugadores[i].append([carta])

        else:

            carta=sacarcarta(baraja)

            listajugadores[i][3].append(carta)

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

def apuestainicialjugadores (listajugadores):

    
    for i in range (len(listajugadores)):

        apuesta=int(input(f" > Introducir apuesta de {listajugadores[i][0]}:"))

        listajugadores[i].append([apuesta])

    return listajugadores

def apuestajugadores (listajugadores,i):

    respuesta=(input(f" > Vas a subir la apuesta {listajugadores[i][0]}?"))

    listasino=["si","no"]

    while respuesta not in listasino:

        respuesta=input("Como? porfavor escriba si o no")

    if respuesta=="si":

        apuesta=int(input(f" > Introduce la apuesta {listajugadores[i][0]}:"))

        listajugadores[i][2].append(apuesta)

def repartircarta (listajugadores,baraja,i):

    carta=sacarcarta(baraja)

    listajugadores[i][3].append(carta)