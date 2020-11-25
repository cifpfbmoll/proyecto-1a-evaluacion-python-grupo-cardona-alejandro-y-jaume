import os
os.system('cls')

import funciones

import objetos

print ("╔════════════════════════════════════════════════════════════════════╗")
print ("║                                                                    ║")
print ("║      Hola y bienvenidos a su programa de BlackJack preferido!      ║")
print ("║                                                                    ║")
print ("╚════════════════════════════════════════════════════════════════════╝")

numerojugadores=int(input("\n>>> Cuantos jugadores vais a jugar?\n >  "))

listajugadores=funciones.nombrejugadores(numerojugadores)

print("\n>>> Con cuanto dinero vais a entrar cada uno?")

funciones.dinerojugadores(listajugadores)
os.system('cls')

print("╔════════════════════════════════════════════════════════════════════╗\n║                                                                    ║\n║                      ¡Que empiece la partida!                      ║\n║                                                                    ║\n╚════════════════════════════════════════════════════════════════════╝")

print ("\n>>> Hagan sus apuestas!\n")

funciones.apuestainicialjugadores(listajugadores)

baraja=funciones.barajar(objetos.baraja)

funciones.repartircartasiniciales(listajugadores,baraja)

#Revelar carta

funciones.repartircartasiniciales(listajugadores,baraja)

for i in range (len(listajugadores)):
    os.system('cls')
    funciones.vercartas(listajugadores,listajugadores[i][0])
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

        funciones.valorcartas(listajugadores[i])

        respuesta=input(">>> Quieres una carta mas?\n >  ")

        while respuesta not in ["si","no"]:

            print("\n ⚠  Porfavor escriba si o no")
            respuesta=input(">>> Quieres una carta mas?\n >  ")

    os.system('cls')

    if i != len(listajugadores)-1:
        print("╔════════════════════════════════════════════════════════════════════╗\n║                                                                    ║\n║                 Vale! pasemos al siguiente jugador                 ║\n║                                                                    ║\n╚════════════════════════════════════════════════════════════════════╝")
        
        input(">>> Pulsa ENTER para pasar al siguiente jugador.\n >  ")

funciones.vermesa(listajugadores)

print (listajugadores)