import os
os.system('cls')

import funciones

import objetos

#Se imprime dos veces looser cuando el ultimo jugador en hablar pierde
#Hacer que el jugador 1 vaya rotando en cada ronda.
#Hacer lista de la banca [Dinero,[cartas],valorcartas] y sus funciones

funciones.colorreset()
print ("╔════════════════════════════════════════════════════════════════════╗")
print ("║                                                                    ║")
print ("║      Hola y bienvenidos a su programa de BlackJack preferido!      ║")
print ("║                                                                    ║")
print ("╚════════════════════════════════════════════════════════════════════╝")

numerojugadores=int(funciones.colorinput("\n>>> Cuantos jugadores vais a jugar?"))

while numerojugadores>7 or numerojugadores<1:

    numerojugadores=int(funciones.colorinput("\n>>> Piensa que solo podeis jugar de 1 a 7 jugadores. Cuantos jugadores vais a jugar?"))

listajugadores=funciones.nombrejugadores(numerojugadores)

print("\n>>> Con cuanto dinero vais a entrar cada uno?")

funciones.dinerojugadores(listajugadores)

opcion=""

while opcion!="terminar":

    os.system('cls')

    print("╔════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                        ║")
    print("║                        ¡Que empiece la partida!                        ║")
    print("║                                                                        ║")
    print("╚════════════════════════════════════════════════════════════════════════╝")

    print ("\n>>> Hagan sus apuestas!\n")

    funciones.apuestainicialjugadores(listajugadores)

    baraja=funciones.barajar(objetos.baraja)

    funciones.repartircartasiniciales(listajugadores,baraja)

    funciones.repartircartasiniciales(listajugadores,baraja)

    for i in range (len(listajugadores)):
        os.system('cls')
        funciones.valorcartas(listajugadores[i])
        funciones.vercartas(listajugadores,listajugadores[i][0])
        respuesta=funciones.colorinput(f">>> Quieres una carta mas {listajugadores[i][0]}?")

        while respuesta not in ["si","no"]:

            funciones.colorerror("\n ⚠  Porfavor escriba si o no")
            respuesta=funciones.colorinput(f">>> Quieres una carta mas {listajugadores[i][0]}?\n >  ")

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

                respuesta=funciones.colorinput(">>> Quieres una carta mas?")

                while respuesta not in ["si","no"]:

                    funciones.colorerror("\n ⚠  Porfavor escriba si o no")
                    respuesta=funciones.colorinput(">>> Quieres una carta mas?")
                os.system('cls')

            if pasado:

                respuesta="no"


        os.system('cls')

        if i != len(listajugadores)-1:
            print("╔════════════════════════════════════════════════════════════════════╗")
            print("║                                                                    ║")
            print("║                 Vale! pasemos al siguiente jugador                 ║")
            print("║                                                                    ║")
            print("╚════════════════════════════════════════════════════════════════════╝")
            
            funciones.colorinput(">>> Pulsa ENTER para pasar al siguiente jugador.")

    funciones.vermesa(listajugadores)

    print ("MENU DEL JUEGO")

    print ("Aqui cada jugador puede salir de la partida o añadir dinero!\n\
Ademas pueden entrar a jugar mas personas mientras se respete el numero maximo de jugadores.")

    for i in range(len(listajugadores)):

        opcion=funciones.colorinput(f"{listajugadores[i][0]} Escribe salir si quieres salir de la partida, añadir si quieres añadir dinero o \
pulsa cualquier otra cosa para seguir jugando asi:")

        if opcion=="salir":

            print (f"Vale! Hasta la proxima {listajugadores[i][0]}!")#si surt un jugador que no sigui es darrer, sa llista s'altere

            del listajugadores[i]

        elif opcion=="añadir":

            dinero=int(funciones.colorinput("Cuanto dinero quieres añadir?"))

            dinerototal=listajugadores[i][1]+dinero

            del listajugadores[i][1]

            listajugadores[i].insert(1,dinerototal)

        else:

            ("Seguimos asi pues!")

    if (len(listajugadores))<7:

        masjugadores=funciones.colorinput("Van a entrar a jugar mas jugadores?")

        if masjugadores=="si":

            numeroNuevosJugadores=int(funciones.colorinput("Cuantos jugadores se van a añadir?"))

            while (len(listajugadores))+numeroNuevosJugadores>7:

                numeroNuevosJugadores=int(funciones.colorinput("No se pueden añadir tantos jugadores! recordad que el maximo son 7!"))

            #Nombre jugador

            #Dinero jugador

        if masjugadores=="no":

            ("Sigamos pues!")

    print (listajugadores)



print (listajugadores)

funciones.colorinput("\n>>> Pulsa ENTER para cerrar el programa.")
