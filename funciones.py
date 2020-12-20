import objetos
import prints
import os

###########################
#          JUEGO          #
###########################

# Función que remueve el primer valor de una lista y lo devuelve, sirve para sacar la primera carta de la baraja.
def sacarCarta (lista): 
    carta=lista.pop(0)
    return carta
# Procedimiento que por cada jugador llama a la función sacarCarta para que le dé una carta y la añade a la lista del jugador.
def repartirCartasIniciales (listajugadores,baraja):
    for i in range (len(listajugadores)):
        carta=sacarCarta(baraja)
        if listajugadores[i][-1]==listajugadores[i][2]:
            listajugadores[i].append([carta])
        else:
            listajugadores[i][3].append(carta)
# Procedimiento que llama a la funcion sacarCarta para que le dé una carta y la añade a la lista de la banca.
def repartirCartaBanca (listabanca,baraja):
    carta=sacarCarta(baraja)
    if listabanca[-1]==listabanca[0]:
        listabanca.append([carta])
    else:
        listabanca[1].append(carta)
# Procedimiento en el cual se utiliza un bucle para ir sacando elementos(cartas) de una lista, para luego buscar el valor de esos elementos en
# un diccionario y sumarlos. Esa suma se añade a la lista de la banca y es el valor actual de las cartas que tiene la banca.
def valorCartasBanca (listabanca):
    valormano=0
    for i in listabanca[1]:
        valormano+=objetos.valor_baraja.get(i)
    valormano=comprobarAses(valormano,listabanca,1)#Comprueba si hay ases para cambiarlos a valor 1 si el jugador se pasa
    if listabanca[-1]==listabanca[1]:
        listabanca.append(valormano)
    else:
        del listabanca[2]
        listabanca.append(valormano)
# Función que aleatoriza los elementos de una lista.
def barajar (lista):
    import random
    random.shuffle(lista)
    return lista
# Procedimiento que añade un numero(dinero) a la lista banca después de limpiarla. Se pedirá el numero hasta que sea mayor que 50.
def dineroBanca (listabanca):
    dineroBanca=int(prints.colorinput("Cuanto dinero quieres que tenga la banca?"))
    while dineroBanca<50:
        prints.colorerror("    ⚠  La banca no tiene suficiente dinero, necesita minimo 50.")
        dineroBanca=int(prints.colorinput("Cuanto dinero quieres que tenga la banca?"))
    listabanca.clear()
    listabanca.append(dineroBanca)
# Función que pide un numero(numero de jugadores) y se asegura que este entre el 1 y el 7. Luego devuelve ese numero.
def cantidadJugadores ():
    numeroJugadores=prints.colorinput("Cuantos jugadores vais a entrar? [1-7]")
    while numeroJugadores not in ["1","2","3","4","5","6","7"]:
        limpiarTerminal()
        prints.creando()
        prints.colorerror("\n    ⚠  Has de seleccionar un número del 1 al 7.")
        numeroJugadores=prints.colorinput("Cuantos jugadores vais a entrar? [1-7]")
    return numeroJugadores
# Función que pide los nombres de los jugadores y finaliza devolviendo la lista de jugadores en cuestión.
def nombreJugadores (numerojugadores):
    listajugadores=[]
    for i in range(1,numerojugadores+1):
        nombrejugador=str(prints.colorinput(f"Escribe el nombre del jugador {i}:"))
        listajugadores.append([nombrejugador.capitalize()])
    return listajugadores
# Procedimiento que pide el dinero con el que jugarán los jugadores y acaba añadiendo esas cantidades dentro de la lista de jugadores.
def dineroJugadores (listajugadores):
    print("   >>> Con cuanto dinero vais a entrar cada uno?\n")
    for i in range (len(listajugadores)):
        dinero=int(prints.colorinput(f"Introducir dinero de {listajugadores[i][0]}:"))
        listajugadores[i].append(dinero)
# Procedimiento que empieza pidiendo las apuestas iniciales (de antes de comenzar la partida) a los jugadores y finaliza añadiendo ese valor a la lista de jugadores.
def apuestaInicialJugadores (listajugadores):
    print ("   >>> Hagan sus apuestas!\n")
    for i in range (len(listajugadores)):
        apuesta=int(prints.colorinput(f"Introducir apuesta de {listajugadores[i][0]}: [ Dinero → {listajugadores[i][1]} ]"))
        while apuesta>listajugadores[i][1] or apuesta<1:
            if apuesta>listajugadores[i][1]:
                prints.colorerror(f"    ⚠  No puedes apostar mas dinero del que tienes en mesa!")
            else:
                prints.colorerror(f"    ⚠  Recuerda que la apuesta minima es de 1 euro!")
            apuesta=int(prints.colorinput(f"Introducir apuesta de {listajugadores[i][0]} [ Dinero → {listajugadores[i][1]} ]"))
        listajugadores[i].append(apuesta)
# Procedimiento que pide al jugador si va a querer o no doblar su apuesta inicial antes de que robe cartas. Si el jugador decide doblar se modifica el valor de su apuesta y se añade el doble.
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
# Procedimiento que añade las cartas a la lista de jugadores.
def repartirCarta (listajugadores,baraja,i):
    carta=sacarCarta(baraja)
    listajugadores[i][3].append(carta)
# Función que pide si el jugador va a querer una carta más para jugar donde finalmente se devolverá la opción seleccionada.
def preguntaUnaCartaMas (jugador):
    respuesta=prints.colorinput(f"Quieres una carta mas {jugador}? [ si / NO ]")
    while respuesta not in ["si","no","SI","NO","Si","No","sí","SÍ","Sí",""]:
        prints.colorerror("    ⚠  Porfavor escriba si o no")
        respuesta=prints.colorinput(f"Quieres una carta mas {jugador}? [ si / NO ]")
    return respuesta
# Función en la cual se utiliza un bucle para ir sacando elementos(cartas) de una lista, para luego buscar el valor de esos elementos en
# un diccionario y sumarlos. Se devuelve ese valor.
def calcularValorMano (listajugadores):
    valormano=0
    for i in listajugadores[3]:
        valormano+=objetos.valor_baraja.get(i)
    valormano=comprobarAses(valormano,listajugadores,3)#Comprueba si hay ases para cambiarlos a valor 1 si el jugador se pasa
    return valormano
# Procedimiento que llama a la funcion calcularValorMano y añade el valor que se da (valor mano jugador) a la lista del jugador.
def valorCartasSimple (listajugadores):
    valormano=calcularValorMano(listajugadores)
    if listajugadores[-1]==listajugadores[3]:
        listajugadores.append(valormano)
    else:
        del listajugadores[4]
        listajugadores.append(valormano)
# Función que llama a la funcion calcularValorMano y añade el valor que se da (valor mano jugador) a la lista del jugador, ademas comprueba si
# el jugador se ha pasado de 21 puntos, si se ha pasado le quita el dinero de la apuesta de su dinero total i se lo suma a la banca. Al final
# devuelve un boleano que hacer referencia a si se ha pasado o no.
def valorCartas (listajugadores,listabanca): 
    apuesta=listajugadores[2]
    valormano=calcularValorMano(listajugadores)
    if listajugadores[-1]!=listajugadores[3]:
        del listajugadores[4]
    listajugadores.append(valormano)
    if valormano>21:
        prints.colorerror("\n   !!! Tu puntuación es mayor a 21.")
        dinerojugador=(listajugadores.pop(1))-apuesta
        listajugadores.insert(1,dinerojugador)
        dineroBanca=listabanca.pop(0)+apuesta
        listabanca.insert(0,dineroBanca)
        pasado=True
        prints.colorinput("Pulsa ENTER para abandonar la mesa.")
    else:
        pasado=False
    return pasado
# Procedimiento utilizado para mostrar la información de la banca en el juego
def verBanca (listabanca):
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
# Procedimiento que muestra las cartas de todos los jugadores en la mesa incluida la banca. Se va utilizando según los jugadores obtengan cartas nuevas, así como resaltando el jugador actual y ocultando la última carta del resto de jugadores. 
def verCartas (listajugadores,jugador,listabanca):
    for i in range (len(listajugadores)):
        valorCartasSimple(listajugadores[i])
    prints.mesa()
    verBanca(listabanca)
    for i in listajugadores: # Recorre la lista de jugadores
        if i[0] == jugador: # Comprueba si es el jugador actual para mostrar el valor de la mano u ocultarlo
            prints.colorjugadoractual()
            print("   >>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: %s" % (i[0],i[1],i[2],i[4]))
        else:
            prints.colorreset()
            print("   >>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: ?" % (i[0],i[1],i[2]))
        if i[0] == jugador:
            for j in i[3]:                          #Empieza a imprimir las cartas del jugador "i", el cual será el jugador actual
                if j != i[3][-1]:                   #Comprueba si la posición de la carta es la primera o la última
                    if j == i[3][0]:                #para saber como ha de imprimirla
                        print("    >> ", end="")     
                    print("%s" % (j), end=" | ")
                else:
                    print("%s" % (j), end="")
        else:
            for j in i[3]:                          #Aquí imprimirá las cartas del resto, separado ya que no debemos ver la última
                if j != i[3][-1]:                   #carta del resto
                    if j == i[3][0]:
                        print("    >> ", end="")
                    print("%s" % (j), end=" | ")
                else:
                    print("?", end="")
        prints.colorreset()
# Procedimiento que muestra todas las cartas de los jugadores mas la banca. Se utiliza al final de la ronda, mostrando la mano final de la banca y todas las cartas de los jugadores.
def verMesa(listajugadores,listabanca):
    prints.mesa()
    verBanca(listabanca)
    for i in listajugadores:
        if listabanca[2] > 21 and i[4] <= 21:       #Determinar si el jugador ha ganado o perdido en funcion de si su puntuacion no supera
            estado = "GANADOR/A"                    #21 y la de la banca si
            prints.colorganador()
        elif i[4] > listabanca[2] and i[4] <= 21:   #Determinar si el jugador ha ganado o perdido en funcion de si su puntuacion supera a la
            estado = "GANADOR/A"                    #de la banca sin pasar de 21
            prints.colorganador()
        else:
            estado = "PERDEDOR/A"                   #Si no se cumple ninguna ha perdido
            prints.colorperdedor()
        print("   >>> Cartas de %s ⁞ Dinero: %s ⁞ Apuesta: %s ⁞ Valor de la mano: %s ⁞ %s" % (i[0],i[1],i[2],i[4],estado))
        for j in i[3]:
            if j != i[3][-1]:                   #Se enseñan todas las cartas, ya que es el final de la partida.
                if j == i[3][0]:
                    print("    >> ", end="")
                print("%s" % (j), end=" | ")
            else:
                print("%s" % (j), end="")
        prints.colorreset()
    if listabanca[0]>0: # Comprueba si la banca se ha quedado sin dinero, para lanzar el mensaje de bancarota o fin de ronda
        print("")
        prints.colorinput("La ronda ha finalizado, pulsa \"ENTER\" para continuar.")
    else:
        print("\n   >>> \033[31mBANCAROTA! \033[92mLa banca se ha quedado sin dinero, coge el dinero antes de que llegue seguridad.")
        prints.colorinput("Pulsa \"ENTER\" para acabar la partida.")
# Función de final de ronda para añadir jugadores al final de ronda
def finAnadirJugadores(listajugadores):
    prints.ronda()
    print("   >>> Aqui cada jugador puede salir de la partida o añadir dinero!\n   >>> Ademas pueden entrar a jugar mas personas mientras se respete el numero máximo de jugadores.\n")
    opcion = opcionesJugadores(listajugadores)
    if len(listajugadores) != 0 and (len(listajugadores)) < 7:
        masjugadores = prints.colorinput(
            "Van a entrar a jugar mas jugadores? [ si / NO ]")
        if masjugadores == "si":
            nuevosJugadores(listajugadores)
        if masjugadores == "no" or masjugadores == "":
            ("   >>> Sigamos pues!")
    return opcion
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
# Función utilizada para acortar código en la funcion de opcionesJugadores(...)
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
# Función utilizada al final de la ronda para saber si los jugadores desean salir de la partida, terminarla, añadir dinero, o continuar
def opcionesJugadores (listajugadores):
    listajugadoressaliendo=[]
    for i in range(len(listajugadores)):
        if len(listajugadores)-1==len(listajugadoressaliendo):
            opcion = gestFinal(listajugadores,i,listajugadoressaliendo,"terminar")
        else:
            opcion = gestFinal(listajugadores,i,listajugadoressaliendo,"salir")
    eliminarJugadores(listajugadoressaliendo,listajugadores)
    return opcion
# Procedimiento utilizado para acortar código en compararCartas(...)
def gestdineroBanca(listabanca,apuesta,i,multiplicador):
    dineroBanca=listabanca.pop(0)-(apuesta*multiplicador)
    listabanca.insert(0,dineroBanca)
    dinerojugador=i.pop(1)+(apuesta*multiplicador)
    i.insert(1,dinerojugador)
def compararCartas (listajugadores,listabanca,tasa_normal,tasa_blackjack):
    for i in listajugadores:#Cuando la banca cobra
        if listabanca[2]<22 and listabanca[2]>=i[4] and i[4]<22: #Si la banca no se pasa, iguala o supera al jugador y el jugador no se ha pasado
            apuesta=i[2]
            dineroBanca=listabanca.pop(0)+apuesta
            listabanca.insert(0,dineroBanca)
            dinerojugador=i.pop(1)-apuesta
            i.insert(1,dinerojugador)
    for i in listajugadores:#Cuando la banca paga
        if (listabanca[2]>21 and i[4]<22 and listabanca[0]>0) or (listabanca[2]<i[4] and i[4]<22 and listabanca[0]>0): #Si la banca se pasa de 21 y el jugador no (y la banca tiene dinero) o si la banca no supera al jugador y el jugador no se ha pasado (y la banca tiene dinero)
            if i[4]==21 and len(i[3])==2:#Si el jugador tiene blackjack
                apuesta=i[2]
                if apuesta*2>listabanca[0]:#Si la banca no tiene suficiente dinero para pagar la apuesta entera
                    apuesta=listabanca[0]
                    gestdineroBanca(listabanca,apuesta,i,tasa_normal)
                else:
                    gestdineroBanca(listabanca,apuesta,i,tasa_blackjack)
            else:
                apuesta=i[2]
                if apuesta>listabanca[0]:#Si la banca no tiene suficiente dinero para pagar la apuesta entera
                    apuesta=listabanca[0]
                    gestdineroBanca(listabanca,apuesta,i,tasa_normal)
                else:
                    gestdineroBanca(listabanca,apuesta,i,tasa_normal)
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

#############################
#          MENUSES          #
#############################

# Función de las opciones para modificar el multiplicador de las tasas
def modificarTasas(tasa_normal,tasa_blackjack):
    tasa_normal = int(prints.colorinput("¿Por cuanto quieres multiplicar la apuesta normal? [Recomendado: 1] [Actual: %d]" % tasa_normal))
    tasa_blackjack = int(prints.colorinput("¿Por cuanto quieres multiplicar la apuesta de BlackJack? [Recomendado: 2] [Actual: %d]" % tasa_blackjack))
    return tasa_normal,tasa_blackjack
# Función utilizada en el menú de opciones para refrescar las variables mostradas en el menú despues de actualizarlas.
def menuOpcionesLimpiar(listabanca,tasa_normal,tasa_blackjack, baraja):
    limpiarTerminal()
    prints.opciones(listabanca[0],tasa_normal,tasa_blackjack, baraja)
    opcion = prints.colorinput("Que deseas hacer?")
    return opcion
# Función usada en los menús para confirmar que la opción seleccionada sea válida
def comprobarOpcion(menu, lista, variable, opcion, listabanca, tasa_normal, tasa_blackjack, baraja):
    while opcion not in lista:
        limpiarTerminal()
        if menu == "opciones":
            prints.opciones(listabanca[0], tasa_normal, tasa_blackjack, baraja)
        else:
            prints.inicio()
        prints.colorerror("    ⚠  Esta opción no está disponible")
        opcion = prints.colorinput(f"Que deseas hacer? {variable}")
    return opcion
# Función utilizada en las opciones para modificar la cantidad de barajas con las que se quiere jugar
def modificarBarajas(baraja):
    baraja_final = int(prints.colorinput("Con cuantas barajas quieres jugar? [Recomendado: 8]"))
    while baraja_final < 1:         # Verificar que haya almenos 1 baraja para jugar
        prints.colorerror("    ⚠  Has de jugar como mínimo con 1 baraja.")
        baraja_final = int(prints.colorinput("Con cuantas barajas quieres jugar? [Recomendado: 8]"))
    return baraja_final
# Función utilizada para mostrar un menú de opciones dónde modificar varias variables sobre el funcionamiento del juego.
def menuOpciones(listabanca,tasa_normal,tasa_blackjack,baraja):
    prints.opciones(listabanca[0], tasa_normal, tasa_blackjack, baraja)
    opcion = prints.colorinput("Que deseas hacer?")
    opcion = comprobarOpcion( "opciones", ["1", "2", "3", "4"], "[ 1 - 4 ]", opcion, listabanca,tasa_normal,tasa_blackjack, baraja)
    while opcion < "4":                                                                 # OPC 1: DINERO BANCA
        if opcion == "1":                                                               # OPC 2: MODIFICAR TASAS
            dineroBanca(listabanca)                                                     # OPC 3: MODIFICAR BARAJAS
        if opcion == "2":                                                               # OPC 4: Salir
            tasa_normal,tasa_blackjack=modificarTasas(tasa_normal,tasa_blackjack)
        if opcion == "3":
            baraja=modificarBarajas(baraja)
        opcion = comprobarOpcion( "opciones", ["1", "2", "3", "4"], "[ 1 - 4 ]", opcion, listabanca,tasa_normal,tasa_blackjack, baraja)
        opcion = menuOpcionesLimpiar(listabanca,tasa_normal,tasa_blackjack, baraja)
    return tasa_normal, tasa_blackjack, baraja
# Función utilizada para acortar código de menuPrincipal(...)
def menuPrincipalInit():
    limpiarTerminal()
    prints.inicio()
    opcion = prints.colorinput("Que deseas hacer? [ 1 - 4 ]")
    return opcion
# Función utilizada para mostrar un menú principal al inicio del programa donde poder entrar en OPCIONES, visualizar las REGLAS, EMPEZAR la partida, o SALIR del programa. Al acabar una partida se vuelve a este menú.
def menuPrincipal(listabanca, tasa_normal, tasa_blackjack, baraja):
    opcion = menuPrincipalInit()
    opcion = comprobarOpcion( "principal", ["1", "2", "3", "4"], "[ 1 - 4 ]", opcion, listabanca,tasa_normal,tasa_blackjack, baraja)
    while opcion < "3":
        if opcion == "1":
            limpiarTerminal()
            tasa_normal,tasa_blackjack,baraja=menuOpciones(listabanca,tasa_normal,tasa_blackjack,baraja)
        if opcion == "2":
            limpiarTerminal()
            prints.reglas()
        opcion = menuPrincipalInit()
        opcion = comprobarOpcion( "principal", ["1", "2", "3", "4"], "[ 1 - 4 ]", opcion, listabanca,tasa_normal,tasa_blackjack, baraja)
    return opcion, tasa_normal, tasa_blackjack, baraja

################################
#          Miscelánea          #
################################

def limpiarTerminal ():
    if os.name=="posix":
        os.system('clear')
    else:
        os.system('cls')
