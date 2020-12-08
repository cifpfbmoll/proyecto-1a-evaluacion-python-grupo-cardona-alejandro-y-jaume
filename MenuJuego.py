import os
os.system('cls')

import funciones
import prints
import objetos

listabanca=[1000000]

#Tenemos que elegir un minimo y maximo de dinero para la banca y con cuanto dinero minimo i maximo pueden entrar los jugadores comparado con la banca.
#Elegir valor de as (creo que lo mejor es darle valor de 1, y luego elegir si subirlo a 11)
#Añadir datos banca a la interfaz visual
#Mirar todas las condiciones donde no se pueda apostar una cantidad debido a que no tiene suficiente dinero el jugador(doblar,...)
#Poner codigo para cuando el jugador o la banca se quedan sin dinero(jugador recomprar o salir), banca=bancarota i cerrar programa.


prints.inicio()
funciones.dinerobanca(listabanca)
numerojugadores=prints.colorinput("\n   >>> Cuantos jugadores vais a jugar? [1-7]")

while numerojugadores not in ["1","2","3","4","5","6","7"]:
    os.system('cls')
    prints.inicio()
    prints.colorerror("\n    ⚠  Has de seleccionar un número del 1 al 7.")
    numerojugadores=prints.colorinput("   >>> Cuantos jugadores vais a jugar? [1-7]")

os.system('cls')
prints.inicio()

listajugadores=funciones.nombrejugadores(int(numerojugadores))

os.system('cls')
prints.inicio()

print("   >>> Con cuanto dinero vais a entrar cada uno?\n")
funciones.dinerojugadores(listajugadores)

os.system('cls')
prints.inicio()

opcion=""

while opcion!="terminar":
    os.system('cls')
    prints.empezar()
    print ("   >>> Hagan sus apuestas!\n")
    funciones.apuestainicialjugadores(listajugadores)
    baraja=funciones.barajar(objetos.baraja[:])
    funciones.repartircartasiniciales(listajugadores,baraja)
    funciones.repartircartabanca(listabanca,baraja)
    funciones.repartircartasiniciales(listajugadores,baraja)
    for i in range (len(listajugadores)):
        os.system('cls')
        funciones.valorcartas(listajugadores[i],listabanca)
        funciones.vercartas(listajugadores,listajugadores[i][0],listabanca)
        respuesta=prints.colorinput(f"   >>> Quieres una carta mas {listajugadores[i][0]}?  [si/NO]")
        while respuesta not in ["si","no","SI","NO","Si","No","sí","SÍ","Sí",""]:
            prints.colorerror("    ⚠  Porfavor escriba si o no")
            respuesta=prints.colorinput(f"   >>> Quieres una carta mas {listajugadores[i][0]}?  [si/NO]")
        vecesdoblado=0
        while respuesta==("si"):
            while vecesdoblado==0:
                funciones.apuestajugadores(listajugadores,i)
                os.system('cls')
                vecesdoblado=1
            
            funciones.repartircarta(listajugadores,baraja,i)
            funciones.vercartas(listajugadores,listajugadores[i][0],listabanca)
            pasado=funciones.valorcartas(listajugadores[i],listabanca)
            
            if not pasado:
                respuesta=prints.colorinput("   >>> Quieres una carta mas? [si/NO]")
                while respuesta not in ["si","no",""]:
                    prints.colorerror("    ⚠  Porfavor escriba si o no")
                    respuesta=prints.colorinput("   >>> Quieres una carta mas? [si/NO]")
                os.system('cls')
            if pasado:
                respuesta="no"
        os.system('cls')
        if i != len(listajugadores)-1:
            prints.siguiente_jugador()
            
            prints.colorinput("   >>> Pulsa \"ENTER\" para pasar al siguiente jugador.")

    #funciones.vermesa(listajugadores,listabanca)
    funciones.valorcartasbanca(listabanca)
    while listabanca[2]<17: #La banca saca cartas hasta que obtiene un valor de 17 o mas
        funciones.repartircartabanca(listabanca,baraja)
        funciones.valorcartasbanca(listabanca)
    funciones.compararcartas(listajugadores,listabanca)
    os.system('cls')
    funciones.vermesa(listajugadores,listabanca)
    funciones.eliminardatosronda(listajugadores)
    del listabanca[1:]
    os.system('cls')
    opcion=funciones.menujuego(listajugadores) #Menu de cuando finaliza la ronda, se devuelve valor porque si  opcion="terminar" se rompe el bucle y termina la partida
    if len(listajugadores)!=0:
        primerJugador=listajugadores.pop(0) #El jugador que hablaba primero pasa a hablar el ultimo
        listajugadores.append(primerJugador)
    #print (baraja)
    #print (listajugadores)
    #print (listabanca)

#print (listajugadores)
#print (listabanca)
os.system('cls')
prints.adios()
prints.colorinput("\n   >>> Pulsa \"ENTER\" para cerrar el programa.")
