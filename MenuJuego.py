import funciones

import objetos


print ("Hola y bienvenidos! a su programa de BlackJack preferido!")

numerojugadores=int(input("Cuantos jugadores vais a jugar?"))

listajugadores=funciones.nombrejugadores(numerojugadores)

print ("Con cuanto dinero vais a entrar cada uno?")

funciones.dinerojugadores(listajugadores)

print ("Vale! empezemos!")

baraja=funciones.barajar(objetos.baraja)

for i in range (len(listajugadores)):

    carta=funciones.sacarcarta(baraja)

    listajugadores[i].append(carta)


