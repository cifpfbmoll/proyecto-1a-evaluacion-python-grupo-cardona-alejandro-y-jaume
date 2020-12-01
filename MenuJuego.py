import os
os.system('cls')

import funciones
import prints
import objetos

#Se imprime dos veces looser cuando el ultimo jugador en hablar pierde
#borrar todos los valores menos nombre i dinero total de las listas al acabar la ronda
#Hacer que el jugador 1 vaya rotando en cada ronda.
#Hacer lista de la banca [Dinero,[cartas],valorcartas] y sus funciones

prints.inicio()

numerojugadores=prints.colorinput("\n>>> Cuantos jugadores vais a jugar? [1-7]")

while numerojugadores not in ["1","2","3","4","5","6","7"]:

    os.system('cls')
    prints.inicio()
    prints.colorerror("\n ⚠  Error. Has de seleccionar un número del 1 al 7.")
    numerojugadores=prints.colorinput(">>> Cuantos jugadores vais a jugar? [1-7]")

listajugadores=funciones.nombrejugadores(int(numerojugadores))

print(">>> Con cuanto dinero vais a entrar cada uno?")

funciones.dinerojugadores(listajugadores)

opcion=""

while opcion!="terminar":

    os.system('cls')

    prints.empezar()

    print ("\n>>> Hagan sus apuestas!\n")

    funciones.apuestainicialjugadores(listajugadores)

    baraja=funciones.barajar(objetos.baraja)

    funciones.repartircartasiniciales(listajugadores,baraja)

    funciones.repartircartasiniciales(listajugadores,baraja)

    for i in range (len(listajugadores)):
        os.system('cls')
        funciones.valorcartas(listajugadores[i])
        funciones.vercartas(listajugadores,listajugadores[i][0])
        respuesta=prints.colorinput(f">>> Quieres una carta mas {listajugadores[i][0]}?  [si/NO]")

        while respuesta not in ["si","no",""]:

            prints.colorerror(" ⚠  Porfavor escriba si o no")
            respuesta=prints.colorinput(f">>> Quieres una carta mas {listajugadores[i][0]}?  [si/NO]")

        vecesdoblado=0

        while respuesta==("si"):

            while vecesdoblado==0:

                funciones.apuestajugadores(listajugadores,i)
                os.system('cls')

                vecesdoblado=1

            funciones.repartircarta(listajugadores,baraja,i)

            funciones.vercartas(listajugadores,listajugadores[i][0])

            pasado=funciones.valorcartas(listajugadores[i])

            if not pasado:

                respuesta=prints.colorinput(">>> Quieres una carta mas? [si/NO]")

                while respuesta not in ["si","no",""]:

                    prints.colorerror(" ⚠  Porfavor escriba si o no")
                    respuesta=prints.colorinput(">>> Quieres una carta mas? [si/NO]")
                os.system('cls')

            if pasado:

                respuesta="no"


        os.system('cls')

        if i != len(listajugadores)-1:
            prints.siguiente_jugador()
            
            prints.colorinput(">>> Pulsa ENTER para pasar al siguiente jugador.")

    funciones.vermesa(listajugadores)

    print ("MENU DEL JUEGO")

    print ("Aqui cada jugador puede salir de la partida o añadir dinero!\n\
Ademas pueden entrar a jugar mas personas mientras se respete el numero maximo de jugadores.")

    listajugadoressaliendo=[]

    for i in range(len(listajugadores)):

        opcion=prints.colorinput(f"{listajugadores[i][0]} Escribe salir si quieres salir de la partida, añadir si quieres añadir dinero o \
pulsa cualquier otra cosa para seguir jugando asi:")

        if opcion=="salir":

            print (f"Vale! Hasta la proxima {listajugadores[i][0]}!")

            listajugadoressaliendo.append(i)

        elif opcion=="añadir":

            dinero=int(prints.colorinput("Cuanto dinero quieres añadir?"))

            dinerototal=listajugadores[i][1]+dinero

            del listajugadores[i][1]

            listajugadores[i].insert(1,dinerototal)

        else:

            ("Seguimos asi pues!")

    listajugadoressaliendo.reverse()

    for i in listajugadoressaliendo:

        del listajugadores[i]

    del listajugadoressaliendo

    if (len(listajugadores))<7:

        masjugadores=prints.colorinput("Van a entrar a jugar mas jugadores?")

        if masjugadores=="si":

            numeroNuevosJugadores=int(prints.colorinput("Cuantos jugadores se van a añadir?"))

            while (len(listajugadores))+numeroNuevosJugadores>7:

                numeroNuevosJugadores=int(prints.colorinput("No se pueden añadir tantos jugadores! recordad que el maximo son 7!"))

            listajugadores.extend(funciones.nombrejugadores(numeroNuevosJugadores))

            funciones.dinerojugadores(listajugadores[-numeroNuevosJugadores:])

            del numeroNuevosJugadores

        if masjugadores=="no":

            ("Sigamos pues!")

    print (listajugadores)



print (listajugadores)

prints.colorinput("\n>>> Pulsa ENTER para cerrar el programa.")
