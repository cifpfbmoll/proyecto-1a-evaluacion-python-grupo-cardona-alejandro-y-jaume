import os
os.system('cls')

import funciones
import prints
import objetos

#Se imprime dos veces looser cuando el ultimo jugador en hablar pierde
#Elegir valor de as (creo que lo mejor es darle valor de 1, y luego elegir si subirlo a 11)
#Hacer lista de la banca [Dinero,[cartas],valorcartas] y sus funciones

prints.inicio()

numerojugadores=prints.colorinput("\n     >>> Cuantos jugadores vais a jugar? [1-7]")

while numerojugadores not in ["1","2","3","4","5","6","7"]:

    os.system('cls')
    prints.inicio()
    prints.colorerror("\n      ⚠  Error. Has de seleccionar un número del 1 al 7.")
    numerojugadores=prints.colorinput("     >>> Cuantos jugadores vais a jugar? [1-7]")

listajugadores=funciones.nombrejugadores(int(numerojugadores))

print("     >>> Con cuanto dinero vais a entrar cada uno?")

funciones.dinerojugadores(listajugadores)

opcion=""

while opcion!="terminar":

    os.system('cls')

    prints.empezar()

    print ("\n     >>> Hagan sus apuestas!\n")

    funciones.apuestainicialjugadores(listajugadores)

    baraja=funciones.barajar(objetos.baraja)

    funciones.repartircartasiniciales(listajugadores,baraja)

    funciones.repartircartasiniciales(listajugadores,baraja)

    for i in range (len(listajugadores)):
        os.system('cls')
        funciones.valorcartas(listajugadores[i])
        funciones.vercartas(listajugadores,listajugadores[i][0])
        respuesta=prints.colorinput(f"     >>> Quieres una carta mas {listajugadores[i][0]}?  [si/NO]")

        while respuesta not in ["si","no","SI","NO","Si","No","sí","SÍ","Sí",""]:

            prints.colorerror("      ⚠  Porfavor escriba si o no")
            respuesta=prints.colorinput(f"     >>> Quieres una carta mas {listajugadores[i][0]}?  [si/NO]")

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

                respuesta=prints.colorinput("     >>> Quieres una carta mas? [si/NO]")

                while respuesta not in ["si","no",""]:

                    prints.colorerror("      ⚠  Porfavor escriba si o no")
                    respuesta=prints.colorinput("     >>> Quieres una carta mas? [si/NO]")
                os.system('cls')

            if pasado:

                respuesta="no"


        os.system('cls')

        if i != len(listajugadores)-1:
            prints.siguiente_jugador()
            
            prints.colorinput("     >>> Pulsa ENTER para pasar al siguiente jugador.")

    funciones.vermesa(listajugadores)

    funciones.eliminardatosronda(listajugadores)

    opcion=funciones.menujuego(listajugadores)

    if len(listajugadores)!=0:

        primerJugador=listajugadores.pop(0) #El jugador que hablaba primero pasa a hablar el ultimo

        listajugadores.append(primerJugador)

    print (listajugadores)

print (listajugadores)

prints.colorinput("\n     >>> Pulsa ENTER para cerrar el programa.")
