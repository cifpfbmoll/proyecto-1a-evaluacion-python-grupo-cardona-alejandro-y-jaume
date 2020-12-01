import objetos
import prints

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

        nombrejugador=str(prints.colorinput(f">>> Escribe el nombre del jugador {i}:"))

        listajugadores.append([nombrejugador.upper()])

    return listajugadores

def dinerojugadores (listajugadores):

    for i in range (len(listajugadores)):

        dinero=int(prints.colorinput(f">>> Introducir dinero de {listajugadores[i][0]}:"))

        listajugadores[i].append(dinero)

    return listajugadores

def apuestainicialjugadores (listajugadores):

    
    for i in range (len(listajugadores)):

        apuesta=int(prints.colorinput(f">>> Introducir apuesta de {listajugadores[i][0]}:"))

        while apuesta>listajugadores[i][1] or apuesta<1:

            if apuesta>listajugadores[i][1]:

                apuesta=int(prints.colorinput(f">>> No puedes apostar mas que el dinero que tienes en mesa! \
introduze una apuesta que puedas cubrir {listajugadores[i][0]}:"))

            else:

                apuesta=int(colorinput(f">>> Recuerda que la apuesta minima es de 1 euro! \
introduce una apuesta superior o igual a 1 euro {listajugadores[i][0]}:"))

        listajugadores[i].append(apuesta)

    return listajugadores

def apuestajugadores (listajugadores,i):

    respuesta=(prints.colorinput(f">>> Vas a doblar la apuesta inicial {listajugadores[i][0]}?"))

    while respuesta not in ["si","no"]:

        prints.colorerror(" ⚠  Porfavor escriba si o no")
        respuesta=(prints.colorinput(f">>> Vas a doblar la apuesta inicial {listajugadores[i][0]}?"))

    if respuesta=="si":

        print (f">>> Muy Bien! Doblemos la apuesta pues {listajugadores[i][0]}")

        apuesta=listajugadores[i][2]

        doblar=apuesta+apuesta

        del listajugadores[i][2]

        listajugadores[i].insert(2,doblar)

def repartircarta (listajugadores,baraja,i):

    carta=sacarcarta(baraja)

    listajugadores[i][3].append(carta)

def valorcartas (listajugadores):

    valormano=0

    apuesta=listajugadores[2]

    for i in listajugadores[3]:

        valormano+=objetos.valor_baraja.get(i)

    if valormano>21:

        if listajugadores[-1]==listajugadores[3]:

            listajugadores.append(valormano)

            print (">>> Looseeeeer!")
            print (">>> Tu puntuación es mayor a 21.")


            dinerojugador=(listajugadores.pop(1))-apuesta

            listajugadores.insert(1,dinerojugador)

            pasado=True

            prints.colorinput("\n>>> Pulsa ENTER para abandonar la mesa.")


        else:

            del listajugadores[4]

            listajugadores.append(valormano)

            print (">>> Looseeeeer!")
            print (">>> Tu puntuación es mayor a 21.")

            dinerojugador=(listajugadores.pop(1))-apuesta

            listajugadores.insert(1,dinerojugador)

            pasado=True

            prints.colorinput("\n>>> Pulsa ENTER para abandonar la mesa.")

    else:

        if listajugadores[-1]==listajugadores[3]:
        
            listajugadores.append(valormano)

            pasado=False

        else:

            del listajugadores[4]

            listajugadores.append(valormano)

            pasado=False

    return pasado

def vercartas (listajugadores,jugador):
    for i in range (len(listajugadores)):
        valorcartas(listajugadores[i])
    print("╔════════════════════════════════════════════════════════════════════════╗\n║                                                                        ║\n║                            Cartas en la mesa                           ║\n║                                                                        ║\n╚════════════════════════════════════════════════════════════════════════╝")
    for i in listajugadores:
        if i[0] == jugador:
            colorjugadoractual()
            print(">>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: %s" % (i[0],i[1],i[2],i[4]))
        else:
            print(">>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: ?" % (i[0],i[1],i[2]))
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
        colorreset()
        print("")


def vermesa(listajugadores):

    print("╔════════════════════════════════════════════════════════════════════════╗\n║                                                                        ║\n║                            Cartas en la mesa                           ║\n║                                                                        ║\n╚════════════════════════════════════════════════════════════════════════╝")
    for i in listajugadores:
        print(">>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: %s" % (i[0],i[1],i[2],i[4]))
        for j in i[3]:
            if j != i[3][-1]:
                print("%s" % (j), end=" | ")
            else:
                print("%s" % (j), end="")
        print("\n")