
from os import system

system("clear")

import funciones

import objetos



print ("Hola y bienvenidos! a su programa de BlackJack preferido!")

numerojugadores=int(input("Cuantos jugadores vais a jugar?"))

listajugadores=funciones.nombrejugadores(numerojugadores)

print ("Con cuanto dinero vais a entrar cada uno?")

funciones.dinerojugadores(listajugadores)

print ("Vale! empezemos!")

print ("Hagan sus apuestas!")

funciones.apuestainicialjugadores(listajugadores)

baraja=funciones.barajar(objetos.baraja)

funciones.repartircartasiniciales(listajugadores,baraja)

#Revelar carta

funciones.repartircartasiniciales(listajugadores,baraja)

for i in range (len(listajugadores)):

    respuesta=input(f"Quieres una carta mas {listajugadores[i][0]}? ")

    #while respuesta!="si" or "no":

        #respuesta=input("Como? porfavor escriba si o no: ")

    while respuesta==("si"):

        funciones.apuestajugadores(listajugadores,i)
        
        #Revelar carta tapada

        funciones.repartircarta(listajugadores,baraja,i)

        respuesta=input("Quieres una carta mas?")

        #while respuesta!="si" or "no":

            #respuesta=input("Como? porfavor escriba si o no: ")



            



print (listajugadores)