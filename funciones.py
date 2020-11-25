import objetos

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

        nombrejugador=str(input(f">>> Escribe el nombre del jugador {i}:\n >  "))

        listajugadores.append([nombrejugador])

    return listajugadores

def dinerojugadores (listajugadores):

    for i in range (len(listajugadores)):

        dinero=int(input(f">>> Introducir dinero de {listajugadores[i][0]}:\n >  "))

        listajugadores[i].append(dinero)

    return listajugadores

def apuestainicialjugadores (listajugadores):

    
    for i in range (len(listajugadores)):

        apuesta=int(input(f">>> Introducir apuesta de {listajugadores[i][0]}:\n >  "))

        listajugadores[i].append([apuesta])

    return listajugadores

def apuestajugadores (listajugadores,i):

    respuesta=(input(f">>> Vas a subir la apuesta {listajugadores[i][0]}?\n >  "))

    while respuesta not in ["si","no"]:

        respuesta=input(" ⚠  Porfavor escriba si o no")

    if respuesta=="si":

        apuesta=int(input(f">>> Introduce la apuesta {listajugadores[i][0]}:\n >  "))

        listajugadores[i][2].append(apuesta)

def repartircarta (listajugadores,baraja,i):

    carta=sacarcarta(baraja)

    listajugadores[i][3].append(carta)

def valorcartas (listajugadores):

    valormano=0

    apuesta=0

    for i in listajugadores[3]:

        valormano+=objetos.valor_baraja.get(i)

    for i in listajugadores[2]:

        apuesta+=i

    if valormano>21:

        print ("Looseeeeer!")

        dinerojugador=(listajugadores.pop(1))-apuesta

        listajugadores.insert(1,dinerojugador)

        pasado=True

    else:

        if listajugadores[-1]==listajugadores[3]:
        
            listajugadores.append([valormano])

            pasado=False

        else:

            del listajugadores[4]

            listajugadores.append([valormano])

            pasado=False

    return pasado

def vercartas (listajugadores,jugador):
    
    print ("╔════════════════════════════════════════════════════════════════════╗\n║                                                                    ║\n║                          Cartas en la mesa                         ║\n║                                                                    ║\n╚════════════════════════════════════════════════════════════════════╝")
    for i in listajugadores:
        print(">>> Cartas de %s" % (i[0]))
        if i[0] == jugador:
            for j in i[3]:
                if j != i[3][-1]:
                    print("%s" % (j), end=" | ")
                else:
                    print("%s" % (j), end="")
        else:
            for j in i[3]:
                if j != i[3][-1]:
                    print("%s" % (j), end=" | ")
                else:
                    print("?", end="")
        print("\n")

def vermesa(listajugadores):

    print ("╔════════════════════════════════════════════════════════════════════╗\n║                                                                    ║\n║                          Cartas en la mesa                         ║\n║                                                                    ║\n╚════════════════════════════════════════════════════════════════════╝")
    for i in listajugadores:
        print(">>> Cartas de %s" % (i[0]))
        for j in i[3]:
            if j != i[3][-1]:
                print("%s" % (j), end=" | ")
            else:
                print("%s" % (j), end="")
        print("\n")