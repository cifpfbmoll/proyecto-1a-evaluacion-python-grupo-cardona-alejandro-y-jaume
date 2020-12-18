import objetos
import prints
import os
def sacarCarta (lista):
    carta=lista.pop(0)
    return carta
def repartirCartasIniciales (listajugadores,baraja):
    for i in range (len(listajugadores)):
        carta=sacarCarta(baraja)
        if listajugadores[i][-1]==listajugadores[i][2]:
            listajugadores[i].append([carta])
        else:
            listajugadores[i][3].append(carta)
def repartirCartaBanca (listabanca,baraja):
    carta=sacarCarta(baraja)
    if listabanca[-1]==listabanca[0]:
        listabanca.append([carta])
    else:
        listabanca[1].append(carta)
def valorCartasBanca (listabanca):
    valormano=0
    for i in listabanca[1]:
        valormano+=objetos.valor_baraja.get(i)
    valormano=comprobarAses(valormano,listabanca,1)
    if listabanca[-1]==listabanca[1]:
        listabanca.append(valormano)
    else:
        del listabanca[2]
        listabanca.append(valormano)
def barajar (lista):
    import random
    random.shuffle(lista)
    return lista
def dineroBanca (listabanca):
    dineroBanca=int(prints.colorinput("Cuanto dinero quieres que tenga la banca?"))
    while dineroBanca<50:
        prints.colorerror("    ⚠  La banca no tiene suficiente dinero, necesita minimo 50.")
        dineroBanca=int(prints.colorinput("Cuanto dinero quieres que tenga la banca?"))
    listabanca.clear()
    listabanca.append(dineroBanca)

def cantidadJugadores ():
    numeroJugadores=prints.colorinput("Cuantos jugadores vais a entrar? [1-7]")
    while numeroJugadores not in ["1","2","3","4","5","6","7"]:
        os.system('cls')
        prints.creando()
        prints.colorerror("\n    ⚠  Has de seleccionar un número del 1 al 7.")
        numeroJugadores=prints.colorinput("Cuantos jugadores vais a entrar? [1-7]")
    return numeroJugadores
def nombreJugadores (numerojugadores):
    listajugadores=[]
    for i in range(1,numerojugadores+1):
        nombrejugador=str(prints.colorinput(f"Escribe el nombre del jugador {i}:"))
        listajugadores.append([nombrejugador.capitalize()])
    return listajugadores
def dineroJugadores (listajugadores):
    for i in range (len(listajugadores)):
        dinero=int(prints.colorinput(f"Introducir dinero de {listajugadores[i][0]}:"))
        listajugadores[i].append(dinero)
    return listajugadores
def apuestaInicialJugadores (listajugadores):
    for i in range (len(listajugadores)):
        apuesta=int(prints.colorinput(f"Introducir apuesta de {listajugadores[i][0]}: [ Dinero → {listajugadores[i][1]} ]"))
        while apuesta>listajugadores[i][1] or apuesta<1:
            if apuesta>listajugadores[i][1]:
                prints.colorerror(f"    ⚠  No puedes apostar mas dinero del que tienes en mesa!")
            else:
                prints.colorerror(f"    ⚠  Recuerda que la apuesta minima es de 1 euro!")
            apuesta=int(prints.colorinput(f"Introducir apuesta de {listajugadores[i][0]} [ Dinero → {listajugadores[i][1]} ]"))
        listajugadores[i].append(apuesta)
    return listajugadores
def apuestaJugadores (listajugadores,i):
    respuesta=(prints.colorinput(f"Vas a doblar la apuesta inicial {listajugadores[i][0]}? [ si / NO ]"))
    while respuesta not in ["si","no","SI","NO","Si","No","sí","SÍ","Sí",""]:
        prints.colorerror("    ⚠  Porfavor escriba si o no")
        respuesta=(prints.colorinput(f"Vas a doblar la apuesta inicial {listajugadores[i][0]}? [ si / NO ]"))
    if respuesta=="si":
        print (f"   >>> Muy Bien! Doblemos la apuesta pues {listajugadores[i][0]}")
        apuesta=listajugadores[i][2]
        doblar=apuesta+apuesta
        del listajugadores[i][2]
        listajugadores[i].insert(2,doblar)
def repartirCarta (listajugadores,baraja,i):
    carta=sacarCarta(baraja)
    listajugadores[i][3].append(carta)
def valorCartasSimple (listajugadores):
    valormano=0
    for i in listajugadores[3]:
        valormano+=objetos.valor_baraja.get(i)
    valormano=comprobarAses(valormano,listajugadores,3)
    if listajugadores[-1]==listajugadores[3]:
        listajugadores.append(valormano)
    else:
        del listajugadores[4]
        listajugadores.append(valormano)
def valorCartas (listajugadores,listabanca):
    valormano=0
    apuesta=listajugadores[2]
    for i in listajugadores[3]:
        valormano+=objetos.valor_baraja.get(i)
    valormano=comprobarAses(valormano,listajugadores,3)
    if valormano>21:
        if listajugadores[-1]!=listajugadores[3]:
            del listajugadores[4]
        listajugadores.append(valormano)
        prints.colorerror("\n   !!! Tu puntuación es mayor a 21.")
        dinerojugador=(listajugadores.pop(1))-apuesta
        listajugadores.insert(1,dinerojugador)
        dineroBanca=listabanca.pop(0)+apuesta
        listabanca.insert(0,dineroBanca)
        pasado=True
        prints.colorinput("Pulsa ENTER para abandonar la mesa.")
    else:
        if listajugadores[-1]!=listajugadores[3]:
            del listajugadores[4]
        listajugadores.append(valormano)
        pasado=False
    return pasado
def verBanca (listabanca):
    #print(listabanca)
    prints.colorbanca()
    valorCartasBanca(listabanca)
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
def verCartas (listajugadores,jugador,listabanca):
    for i in range (len(listajugadores)):
        valorCartasSimple(listajugadores[i])
    prints.mesa()
    verBanca(listabanca)
    for i in listajugadores:
        if i[0] == jugador:
            prints.colorjugadoractual()
            print("   >>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: %s" % (i[0],i[1],i[2],i[4]))
        else:
            prints.colorreset()
            print("   >>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: ?" % (i[0],i[1],i[2]))
        if i[0] == jugador:
            for j in i[3]:                          # Empieza a imprimir las cartas del jugador "i", el cual será el jugador actual
                if j != i[3][-1]:                   # Comprueba si la posicion de la carta es la primera o la ultima
                    if j == i[3][0]:                # para saber como ha de imprimirlaa
                        print("    >> ", end="")     
                    print("%s" % (j), end=" | ")
                else:
                    print("%s" % (j), end="")
        else:
            for j in i[3]:                          # Aqui imprimirá las cartas del resto, separado ya que no debemos ver la ultima
                if j != i[3][-1]:                   # carta del resto
                    if j == i[3][0]:
                        print("    >> ", end="")
                    print("%s" % (j), end=" | ")
                else:
                    print("?", end="")
        prints.colorreset()
def verMesa(listajugadores,listabanca):
    prints.mesa()
    verBanca(listabanca)
    for i in listajugadores:
        if listabanca[2] > 21 and i[4] <= 21:   # Determinar si el jugador ha ganado o perdido
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
            if j != i[3][-1]:                   # Se enseñan todas las cartas ya que es el final de la partida.
                if j == i[3][0]:
                    print("    >> ", end="")
                print("%s" % (j), end=" | ")
            else:
                print("%s" % (j), end="")
        prints.colorreset()
    if listabanca[0]>0:
        print("")
        prints.colorinput("La ronda ha finalizado, pulsa \"ENTER\" para continuar.")
    else:
        print("\n   >>> \033[31mBANCAROTA! \033[92mLa banca se ha quedado sin dinero, coge el dinero antes de que llegue seguridad.")
        prints.colorinput("Pulsa \"ENTER\" para acabar la partida.")
def eliminarJugadores (listajugadoressaliendo,listajugadores):
    listajugadoressaliendo.reverse()
    for i in listajugadoressaliendo:
        del listajugadores[i]
    del listajugadoressaliendo
def añadirDinero (listajugadores,i):
    dinero=int(prints.colorinput(f"Cuanto dinero quieres añadir? [ Dinero → {listajugadores[i][1]} ]"))
    dinerototal=listajugadores[i][1]+dinero
    del listajugadores[i][1]
    listajugadores[i].insert(1,dinerototal)
def nuevosJugadores (listajugadores):
    numeronuevosJugadores=int(prints.colorinput("Cuantos jugadores se van a añadir?"))
    while (len(listajugadores))+numeronuevosJugadores>7:
        prints.colorerror("    ⚠  El máximo son 7 jugadores.")
        numeronuevosJugadores=int(prints.colorinput("Cuantos jugadores se van a añadir?"))
    listajugadores.extend(nombreJugadores(numeronuevosJugadores))
    dineroJugadores(listajugadores[-numeronuevosJugadores:])
    del numeronuevosJugadores
def eliminarDatosRonda (listajugadores):
    for i in listajugadores:
        del i[2:]
def gestFinal(listajugadores,i,listajugadoressaliendo,opc):
    if listajugadores[i][1]<=0:
        opcion=prints.colorinput(f"{listajugadores[i][0]}, ¿deseas {opc} la partida o añadir dinero? [ {opc} / añadir ]")
        while opcion not in ["%s" % (opc),"añadir"]:
            prints.colorerror("    ⚠  Esta opción no está disponible")
            opcion=prints.colorinput(f"{listajugadores[i][0]}, ¿deseas {opc} la partida o añadir dinero? [ {opc} / añadir ]")
    else:
        opcion=prints.colorinput(f"{listajugadores[i][0]}, ¿deseas {opc} la partida, añadir dinero, o  continuar? [ {opc} / añadir / ENTER ]")
    if opcion=="%s" % (opc):
        print (f"   >>> ¡Vale! Hasta la proxima {listajugadores[i][0]}!")
        listajugadoressaliendo.append(i)
    elif opcion=="añadir":
        añadirDinero (listajugadores,i)
    else:
        ("   >>> ¡Sigamos asi pues!")
    return opcion
def opcionesJugadores (listajugadores):
    listajugadoressaliendo=[]
    for i in range(len(listajugadores)):
        if len(listajugadores)-1==len(listajugadoressaliendo):
            opcion = gestFinal(listajugadores,i,listajugadoressaliendo,"terminar")
        else:
            opcion = gestFinal(listajugadores,i,listajugadoressaliendo,"salir")
    eliminarJugadores(listajugadoressaliendo,listajugadores)
    return opcion
def gestdineroBanca(listabanca,apuesta,i,multiplicador):
    dineroBanca=listabanca.pop(0)-(apuesta*multiplicador)
    listabanca.insert(0,dineroBanca)
    dinerojugador=i.pop(1)+(apuesta*multiplicador)
    i.insert(1,dinerojugador)
def compararCartas (listajugadores,listabanca,apuesta_normal,apuesta_blackjack):
    for i in listajugadores:#Cuando la banca cobra
        if listabanca[2]<22 and listabanca[2]>=i[4] and i[4]<22: #Si la banca no se pasa, iguala o supera al jugador i el jugador no se ha pasado
            apuesta=i[2]
            dineroBanca=listabanca.pop(0)+apuesta
            listabanca.insert(0,dineroBanca)
            dinerojugador=i.pop(1)-apuesta
            i.insert(1,dinerojugador)
    for i in listajugadores:#Cuando la banca paga
        if (listabanca[2]>21 and i[4]<22 and listabanca[0]>0) or (listabanca[2]<i[4] and i[4]<22 and listabanca[0]>0): #Si la banca se pasa de 21 y el jugador no (y la banca tiene dinero) o si la banca no supera al jugador i el jugador no se ha pasado (y la banca tiene dinero)
            if i[4]==21 and len(i[3])==2:#Si el jugador tiene blackjack
                apuesta=i[2]
                if apuesta*2>listabanca[0]:#Si la banca no tiene suficiente dinero para pagar la apuesta entera
                    apuesta=listabanca[0]
                    gestdineroBanca(listabanca,apuesta,i,apuesta_normal)
                else:
                    gestdineroBanca(listabanca,apuesta,i,apuesta_blackjack)
            else:
                apuesta=i[2]
                if apuesta>listabanca[0]:#Si la banca no tiene suficiente dinero para pagar la apuesta entera
                    apuesta=listabanca[0]
                    gestdineroBanca(listabanca,apuesta,i,apuesta_normal)
                else:
                    gestdineroBanca(listabanca,apuesta,i,apuesta_normal)
def comprobarAses(valormano,listajugadores,a):
    if valormano>21:
        hayAs=False
        for i in listajugadores[a]:
            if "AS" in i:
                hayAs=True
        if hayAs:
            ases=0
            for j in listajugadores[a]:
                ases+=j.count("AS")
            for k in range(ases):
                if valormano>21:
                    valormano-=10
    return valormano
def modificarApuestas(apuesta_normal,apuesta_blackjack):
    apuesta_normal = int(prints.colorinput("¿Por cuanto quieres multiplicar la apuesta normal? [Recomendado: 1] [Actual: %d]" % apuesta_normal))
    apuesta_blackjack = int(prints.colorinput("¿Por cuanto quieres multiplicar la apuesta de BlackJack? [Recomendado: 1] [Actual: %d]" % apuesta_blackjack))
    return apuesta_normal,apuesta_blackjack
def menuJuego (listajugadores): 
    prints.ronda()
    print ("   >>> Aqui cada jugador puede salir de la partida o añadir dinero!\n   >>> Ademas pueden entrar a jugar mas personas mientras se respete el numero máximo de jugadores.\n")
    opcion=opcionesJugadores(listajugadores)
    if len(listajugadores)!=0 and (len(listajugadores))<7:
        masjugadores=prints.colorinput("Van a entrar a jugar mas jugadores? [ si / NO ]")
        if masjugadores=="si":
            nuevosJugadores(listajugadores)
        if masjugadores=="no" or masjugadores=="":
            ("   >>> Sigamos pues!")
    return opcion
def menuOpcionesLimpiar(listabanca,apuesta_normal,apuesta_blackjack, baraja):
    os.system('cls')
    prints.opciones(listabanca[0],apuesta_normal,apuesta_blackjack, baraja)
    opcion = prints.colorinput("Que deseas hacer?")
    return opcion
def comprobarOpcion(lista, variable, opcion, listabanca, apuesta_normal, apuesta_blackjack, baraja):
    while opcion not in lista:
        os.system('cls')
        prints.opciones(listabanca[0], apuesta_normal, apuesta_blackjack, baraja)
        prints.colorerror("    ⚠  Esta opción no está disponible")
        opcion = prints.colorinput(f"Que deseas hacer? {variable}")
def modificarBarajas(baraja):
    print(baraja)
    baraja_final = int(prints.colorinput("Con cuantas barajas quieres jugar? [Recomendado: 8]"))
    return baraja_final
def menuOpciones(listabanca,apuesta_normal,apuesta_blackjack,baraja):
    prints.opciones(listabanca[0], apuesta_normal, apuesta_blackjack, baraja)
    opcion = prints.colorinput("Que deseas hacer?")
    comprobarOpcion(["1", "2", "3", "4"], "[ 1 - 4 ]", opcion, listabanca,apuesta_normal,apuesta_blackjack, baraja)
    while opcion < "4":
        comprobarOpcion(["1", "2", "3", "4"], "[ 1 - 4 ]", opcion, listabanca,apuesta_normal,apuesta_blackjack, baraja)
        if opcion == "1":
            dineroBanca(listabanca)
        if opcion == "2":
            apuesta_normal,apuesta_blackjack=modificarApuestas(apuesta_normal,apuesta_blackjack)
        if opcion == "3":
            baraja=modificarBarajas(baraja)
        opcion = menuOpcionesLimpiar(listabanca,apuesta_normal,apuesta_blackjack, baraja)
    return apuesta_normal, apuesta_blackjack, baraja
def menuPrincipalInit():
    os.system('cls')
    prints.inicio()
    opcion = prints.colorinput("Que deseas hacer? [ 1 - 4 ]")
    return opcion


def menuPrincipal(listabanca, apuesta_normal, apuesta_blackjack, baraja):
    opcion = menuPrincipalInit()
    comprobarOpcion(["1", "2", "3", "4"], "[ 1 - 4 ]", opcion, listabanca,apuesta_normal,apuesta_blackjack, baraja)
    while opcion < "3":
        comprobarOpcion(["1", "2", "3", "4"], "[ 1 - 4 ]", opcion, listabanca,apuesta_normal,apuesta_blackjack, baraja)
        if opcion == "1":
            os.system('cls')
            apuesta_normal,apuesta_blackjack,baraja=menuOpciones(listabanca,apuesta_normal,apuesta_blackjack,baraja)
        if opcion == "2":
            os.system('cls')
            prints.reglas()
        opcion = menuPrincipalInit()
    return opcion, apuesta_normal, apuesta_blackjack, baraja
