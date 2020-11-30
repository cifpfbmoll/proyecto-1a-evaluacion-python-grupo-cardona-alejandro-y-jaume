import os
os.system('cls')

import funciones

import objetos

#Hacer bucle de partida i que el jugador 1 vaya rotando en cada ronda.
#Hacer menu del juego donde puedas salir de la partida, añadir jugador o añadir dinero despues de cada partida
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

#Revelar carta

funciones.repartircartasiniciales(listajugadores,baraja)


for i in range (len(listajugadores)):
    os.system('cls')
    funciones.valorcartas(listajugadores[i])
    funciones.vercartas(listajugadores,listajugadores[i][0])
    respuesta=funciones.colorinput(f">>> Quieres una carta mas {listajugadores[i][0]}?")

    while respuesta not in ["si","no"]:

        funciones.colorerror("\n ⚠  Porfavor escriba si o no")
        respuesta=funciones.colorinput(f">>> Quieres una carta mas {listajugadores[i][0]}?")

    vecesdoblado=0

    while respuesta==("si"):

        while vecesdoblado==0:

            funciones.apuestajugadores(listajugadores,i)
            os.system('cls')

            vecesdoblado=1
        
        #Revelar carta tapada

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

print (listajugadores)

funciones.colorinput("\n>>> Pulsa ENTER para cerrar el programa.")
