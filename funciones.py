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

def repartircartabanca (listabanca,baraja):
    if listabanca[-1]==listabanca[0]:
        carta=sacarcarta(baraja)
        listabanca.append([carta])
    else:
        carta=sacarcarta(baraja)
        listabanca[1].append(carta)

def valorcartasbanca (listabanca):
    valormano=0
    for i in listabanca[1]:
        valormano+=objetos.valor_baraja.get(i)
    if listabanca[-1]==listabanca[1]:
        listabanca.append(valormano)
    else:
        del listabanca[2]
        listabanca.append(valormano)

def barajar (lista):
    import random
    random.shuffle(lista)
    return lista

def dinerobanca (listabanca):
    cambio=prints.colorinput("\n   >>> La banca empieza con 1.000.000 de euros.\n   >>> Si quiere cambiar esa cantidad escriba \"CAMBIAR\", si no pulse \"ENTER\".")
    if cambio=="cambiar":
        dinerobanca=int(prints.colorinput("   >>> Cuanto dinero quieres que tenga la banca?"))
        while dinerobanca<50:
            dinerobanca=int(prints.colorinput("   >>> La banca necesita minimo 50 euros, Cuanto dinero quieres que tenga la banca?"))
        listabanca.clear()
        listabanca.append(dinerobanca)

def nombrejugadores (numerojugadores):
    listajugadores=[]
    for i in range(1,numerojugadores+1):
        nombrejugador=str(prints.colorinput(f"   >>> Escribe el nombre del jugador {i}:"))
        listajugadores.append([nombrejugador.capitalize()])
    return listajugadores

def dinerojugadores (listajugadores):
    for i in range (len(listajugadores)):
        dinero=int(prints.colorinput(f"   >>> Introducir dinero de {listajugadores[i][0]}:"))
        listajugadores[i].append(dinero)
    return listajugadores

def apuestainicialjugadores (listajugadores):
    for i in range (len(listajugadores)):
        apuesta=int(prints.colorinput(f"   >>> Introducir apuesta de {listajugadores[i][0]} (Dinero: {listajugadores[i][1]}):"))
        while apuesta>listajugadores[i][1] or apuesta<1:
            if apuesta>listajugadores[i][1]:
                prints.colorerror(f"    ⚠  No puedes apostar mas dinero del que tienes en mesa!")
                apuesta=int(prints.colorinput(f"   >>> Introducir apuesta de {listajugadores[i][0]} (Dinero: {listajugadores[i][1]}):"))
            else:
                prints.colorerror(f"    ⚠  Recuerda que la apuesta minima es de 1 euro!")
                apuesta=int(prints.colorinput(f"   >>> Introducir apuesta de {listajugadores[i][0]} (Dinero: {listajugadores[i][1]}):"))
        listajugadores[i].append(apuesta)
    return listajugadores

def apuestajugadores (listajugadores,i):
    respuesta=(prints.colorinput(f"   >>> Vas a doblar la apuesta inicial {listajugadores[i][0]}?"))
    while respuesta not in ["si","no","SI","NO","Si","No","sí","SÍ","Sí"]:
        prints.colorerror("    ⚠  Porfavor escriba si o no")
        respuesta=(prints.colorinput(f"   >>> Vas a doblar la apuesta inicial {listajugadores[i][0]}?"))
    if respuesta=="si":
        print (f"   >>> Muy Bien! Doblemos la apuesta pues {listajugadores[i][0]}")
        apuesta=listajugadores[i][2]
        doblar=apuesta+apuesta
        del listajugadores[i][2]
        listajugadores[i].insert(2,doblar)

def repartircarta (listajugadores,baraja,i):
    carta=sacarcarta(baraja)
    listajugadores[i][3].append(carta)

def valorcartassimple (listajugadores):
    valormano=0
    for i in listajugadores[3]:
        valormano+=objetos.valor_baraja.get(i)
    if listajugadores[-1]==listajugadores[3]:
        listajugadores.append(valormano)
    else:
        del listajugadores[4]
        listajugadores.append(valormano)

def valorcartas (listajugadores,listabanca):
    valormano=0
    apuesta=listajugadores[2]
    for i in listajugadores[3]:
        valormano+=objetos.valor_baraja.get(i)
    if valormano>21:
        if listajugadores[-1]==listajugadores[3]:
            listajugadores.append(valormano)
            print ("   >>> Looseeeeer!")
            print ("   >>> Tu puntuación es mayor a 21.")
            dinerojugador=(listajugadores.pop(1))-apuesta
            listajugadores.insert(1,dinerojugador)
            dinerobanca=listabanca.pop(0)+apuesta
            listabanca.insert(0,dinerobanca)
            pasado=True
            prints.colorinput("\n   >>> Pulsa ENTER para abandonar la mesa.")
        else:
            del listajugadores[4]
            listajugadores.append(valormano)
            print ("   >>> Looseeeeer!")
            print ("   >>> Tu puntuación es mayor a 21.")
            dinerojugador=(listajugadores.pop(1))-apuesta
            listajugadores.insert(1,dinerojugador)
            dinerobanca=listabanca.pop(0)+apuesta
            listabanca.insert(0,dinerobanca)
            pasado=True
            prints.colorinput("\n   >>> Pulsa ENTER para abandonar la mesa.")
    else:
        if listajugadores[-1]==listajugadores[3]:
            listajugadores.append(valormano)
            pasado=False
        else:
            del listajugadores[4]
            listajugadores.append(valormano)
            pasado=False

    return pasado

def verbanca (listabanca):
    #print(listabanca)
    prints.colorbanca()
    valorcartasbanca(listabanca)
    print("   >>> Cartas de la BANCA ⁞ Dinero: %s ⁞ Valor de la mano: %s" % (listabanca[0],listabanca[2]))
    for i in listabanca[1]:
        if i != listabanca[1][-1]:
            if i == listabanca[1][0]:
                print("    >> ", end="")
            print("%s" % (i), end=" | ")
        else:
            if i == listabanca[1][0]:
                print("    >> ", end="")
            print("%s" % (i), end="")
    prints.colorreset()

def vercartas (listajugadores,jugador,listabanca):
    for i in range (len(listajugadores)):
        valorcartassimple(listajugadores[i])
    prints.mesa()
    verbanca(listabanca)
    for i in listajugadores:
        if i[0] == jugador:
            prints.colorjugadoractual()
            print("   >>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: %s" % (i[0],i[1],i[2],i[4]))
        else:
            prints.colorreset()
            print("   >>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: ?" % (i[0],i[1],i[2]))
        if i[0] == jugador:
            for j in i[3]:
                if j != i[3][-1]:
                    if j == i[3][0]:
                        print("    >> ", end="")
                    print("%s" % (j), end=" | ")
                else:
                    print("%s" % (j), end="")
        else:
            for j in i[3]:
                if j != i[3][-1]:
                    if j == i[3][0]:
                        print("    >> ", end="")
                    print("%s" % (j), end=" | ")
                else:
                    print("?", end="")
        prints.colorreset()

def vermesa(listajugadores,listabanca):
    prints.mesa()
    verbanca(listabanca)
    for i in listajugadores:
        if listabanca[2] > 21 and i[4] <= 21:
            estado = "GANADOR/A"
            prints.colorganador()
        elif i[4] > listabanca[2] and i[4] <= 21:
            estado = "GANADOR/A"
            prints.colorganador()
        else:
            estado = "PERDEDOR/A"
            prints.colorperdedor()
        print("   >>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: %s ⁞ %s" % (i[0],i[1],i[2],i[4],estado))
        for j in i[3]:
            if j != i[3][-1]:
                if j == i[3][0]:
                    print("    >> ", end="")
                print("%s" % (j), end=" | ")
            else:
                print("%s" % (j), end="")
        prints.colorreset()
    prints.colorinput("   >>> La partida ha finalizado, pulsa \"ENTER\" para continuar.")

def eliminarjugadores (listajugadoressaliendo,listajugadores):

    listajugadoressaliendo.reverse()

    for i in listajugadoressaliendo:

        del listajugadores[i]

    del listajugadoressaliendo

def añadirdinero (listajugadores,i):
    dinero=int(prints.colorinput(f"   >>> Cuanto dinero quieres añadir? (Dinero: {listajugadores[i][1]})"))
    dinerototal=listajugadores[i][1]+dinero
    del listajugadores[i][1]
    listajugadores[i].insert(1,dinerototal)

def nuevosjugadores (listajugadores):
    numeroNuevosJugadores=int(prints.colorinput("   >>> Cuantos jugadores se van a añadir?"))
    while (len(listajugadores))+numeroNuevosJugadores>7:
        prints.colorerror("    ⚠  El máximo son 7 jugadores.")
        numeroNuevosJugadores=int(prints.colorinput("   >>> Cuantos jugadores se van a añadir?"))
    listajugadores.extend(nombrejugadores(numeroNuevosJugadores))
    dinerojugadores(listajugadores[-numeroNuevosJugadores:])
    del numeroNuevosJugadores

def eliminardatosronda (listajugadores):
    for i in listajugadores:
        del i[2:]

def opcionesjugadores (listajugadores):
    listajugadoressaliendo=[]
    for i in range(len(listajugadores)):
        if len(listajugadores)-1==len(listajugadoressaliendo):
            if listajugadores[i][1]<=0:
                opcion=prints.colorinput(f"   >>> {listajugadores[i][0]}, ¿deseas terminar la partida o añadir dinero? [ terminar / añadir ]")
                while opcion not in ["terminar","añadir"]:
                    opcion=prints.colorinput(f"   >>> {listajugadores[i][0]}, esa opcion no es posible, solo puedes terminar la partida o añadir dinero [ terminar / añadir ]")
            else:
                opcion=prints.colorinput(f"   >>> {listajugadores[i][0]}, ¿deseas terminar la partida, añadir dinero, o  continuar? [ terminar / añadir / ENTER ]")

            if opcion=="terminar":
                print (f"   >>> ¡Vale! Hasta la proxima {listajugadores[i][0]}!")
                listajugadoressaliendo.append(i)
            elif opcion=="añadir":
                añadirdinero (listajugadores,i)
            else:
                ("   >>> ¡Sigamos asi pues!")
        else:
            if listajugadores[i][1]<=0:
                opcion=prints.colorinput(f"   >>> {listajugadores[i][0]}, ¿deseas salir de la partida o añadir dinero? [ salir / añadir ]")
                while opcion not in ["salir","añadir"]:
                    opcion=prints.colorinput(f"   >>> {listajugadores[i][0]}, esa opcion no es posible, solo puedes salir de la partida o añadir dinero [ salir / añadir ]")
            else:
                opcion=prints.colorinput(f"   >>> {listajugadores[i][0]}, ¿deseas salir la partida, añadir dinero, o  continuar? [ salir / añadir / ENTER ]")

            if opcion=="salir":
                print (f"   >>> ¡Vale! Hasta la proxima {listajugadores[i][0]}!")
                listajugadoressaliendo.append(i)
            elif opcion=="añadir":
                añadirdinero (listajugadores,i)
            else:
                ("   >>> ¡Sigamos asi pues!")
    eliminarjugadores(listajugadoressaliendo,listajugadores)
    return opcion

def menujuego (listajugadores): 

    prints.menu()

    print ("   >>> Aqui cada jugador puede salir de la partida o añadir dinero!\n   >>> Ademas pueden entrar a jugar mas personas mientras se respete el numero máximo de jugadores.\n")

    opcion=opcionesjugadores(listajugadores)

    if len(listajugadores)!=0 and (len(listajugadores))<7:

        masjugadores=prints.colorinput("   >>> Van a entrar a jugar mas jugadores?")

        if masjugadores=="si":

            nuevosjugadores(listajugadores)

        if masjugadores=="no":

            ("   >>> Sigamos pues!")

    return opcion

def compararcartas (listajugadores,listabanca):
    for i in listajugadores:#Cuando la banca cobra
        if listabanca[2]<22 and listabanca[2]>=i[4] and i[4]<22: #Si la banca no se pasa, iguala o supera al jugador i el jugador no se ha pasado
            apuesta=i[2]
            dinerobanca=listabanca.pop(0)+apuesta
            listabanca.insert(0,dinerobanca)
            dinerojugador=i.pop(1)-apuesta
            i.insert(1,dinerojugador)
    for i in listajugadores:#Cuando la banca paga
        if listabanca[2]>21 and i[4]<22 and listabanca[0]>0: #Si la banca se pasa de 21 y el jugador no (y la banca tiene dinero)
            if i[4]==21:#Si el jugador tiene blackjack
                apuesta=i[2]
                if apuesta*2>listabanca[0]:#Si la banca no tiene suficiente dinero para pagar la apuesta entera
                    apuesta=listabanca[0]
                    dinerobanca=listabanca.pop(0)-(apuesta)
                    listabanca.insert(0,dinerobanca)
                    dinerojugador=i.pop(1)+(apuesta)
                    i.insert(1,dinerojugador)
                else:
                    dinerobanca=listabanca.pop(0)-(apuesta*2)
                    listabanca.insert(0,dinerobanca)
                    dinerojugador=i.pop(1)+(apuesta*2)
                    i.insert(1,dinerojugador)
            else:
                apuesta=i[2]
                if apuesta>listabanca[0]:#Si la banca no tiene suficiente dinero para pagar la apuesta entera
                    apuesta=listabanca[0]
                    dinerobanca=listabanca.pop(0)-(apuesta)
                    listabanca.insert(0,dinerobanca)
                    dinerojugador=i.pop(1)+(apuesta)
                    i.insert(1,dinerojugador)
                else:
                    dinerobanca=listabanca.pop(0)-apuesta
                    listabanca.insert(0,dinerobanca)
                    dinerojugador=i.pop(1)+apuesta
                    i.insert(1,dinerojugador)
        elif listabanca[2]<i[4] and i[4]<22 and listabanca[0]>0: #Si la banca no supera al jugador i el jugador no se ha pasado (y la banca tiene dinero)
            if i[4]==21:#Si el jugador tiene blackjack
                apuesta=i[2]
                if apuesta*2>listabanca[0]:#Si la banca no tiene suficiente dinero para pagar la apuesta entera
                    apuesta=listabanca[0]
                    dinerobanca=listabanca.pop(0)-(apuesta)
                    listabanca.insert(0,dinerobanca)
                    dinerojugador=i.pop(1)+(apuesta)
                    i.insert(1,dinerojugador)
                else:
                    dinerobanca=listabanca.pop(0)-(apuesta*2)
                    listabanca.insert(0,dinerobanca)
                    dinerojugador=i.pop(1)+(apuesta*2)
                    i.insert(1,dinerojugador)
            else:
                apuesta=i[2]
                if apuesta>listabanca[0]:#Si la banca no tiene suficiente dinero para pagar la apuesta entera
                    apuesta=listabanca[0]
                    dinerobanca=listabanca.pop(0)-(apuesta)
                    listabanca.insert(0,dinerobanca)
                    dinerojugador=i.pop(1)+(apuesta)
                    i.insert(1,dinerojugador)
                else:
                    dinerobanca=listabanca.pop(0)-apuesta
                    listabanca.insert(0,dinerobanca)
                    dinerojugador=i.pop(1)+apuesta
                    i.insert(1,dinerojugador)