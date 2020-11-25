
from os import system

system("clear")

import funciones

import objetos

print ("\n")
print ("╔════════════════════════════════════════════════════════════════════╗")
print ("║                                                                    ║")
print ("║      Hola y bienvenidos a su programa de BlackJack preferido!      ║")
print ("║                                                                    ║")
print ("╚════════════════════════════════════════════════════════════════════╝")

numerojugadores=int(input("\n>>> Cuantos jugadores vais a jugar?\n >  "))

listajugadores=funciones.nombrejugadores(numerojugadores)

print ("\n>>> Con cuanto dinero vais a entrar cada uno?")

funciones.dinerojugadores(listajugadores)

print ("\n>>> Vale! empezemos!")

print (">>> Hagan sus apuestas!\n")

funciones.apuestainicialjugadores(listajugadores)

baraja=funciones.barajar(objetos.baraja)

funciones.repartircartasiniciales(listajugadores,baraja)

#Revelar carta

funciones.repartircartasiniciales(listajugadores,baraja)

for i in range (len(listajugadores)):

    respuesta=input(f">>> Quieres una carta mas {listajugadores[i][0]}?\n >  ")

    while respuesta not in ["si","no"]:

        print("\n ⚠  Porfavor escriba si o no")
        respuesta=input(f">>> Quieres una carta mas {listajugadores[i][0]}?\n >  ")

    vecesdoblado=0

    while respuesta==("si"):

        while vecesdoblado==0:

            funciones.apuestajugadores(listajugadores,i)

            vecesdoblado=1
        
        #Revelar carta tapada

        funciones.repartircarta(listajugadores,baraja,i)

        respuesta=input(">>> Quieres una carta mas?\n >  ")

        while respuesta not in ["si","no"]:

            print("\n ⚠  Porfavor escriba si o no")
            respuesta=input(">>> Quieres una carta mas?\n >  ")

    print ("Vale! pasemos al siguiente jugador")



print (listajugadores)