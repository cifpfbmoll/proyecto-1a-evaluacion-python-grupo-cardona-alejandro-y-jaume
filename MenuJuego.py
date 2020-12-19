import os
import funciones
import prints
import objetos
listabanca=[1000000]

tasa_normal = 1 
tasa_blackjack = 2
numero_barajas = 8
#Optimizar funciones.
opc,tasa_normal,tasa_blackjack,numero_barajas = funciones.menuPrincipal(listabanca, tasa_normal, tasa_blackjack, numero_barajas)
while opc != "4":
    if opc == "3":
        if listabanca[0]==0:
            funciones.dineroBanca(listabanca)
        numerojugadores=funciones.cantidadJugadores()
        os.system('cls')
        prints.creando()
        listajugadores=funciones.nombreJugadores(int(numerojugadores))
        os.system('cls')
        prints.creando()
        funciones.dineroJugadores(listajugadores)
        os.system('cls')
        prints.creando()
        opcion=""
        while opcion!="terminar":
            os.system('cls')
            prints.empezar()
            funciones.apuestaInicialJugadores(listajugadores)
            baraja=funciones.barajar(objetos.baraja[:]*numero_barajas)
            funciones.repartirCartasIniciales(listajugadores,baraja)
            funciones.repartirCartaBanca(listabanca,baraja)
            funciones.repartirCartasIniciales(listajugadores,baraja)
            for i in range (len(listajugadores)):
                os.system('cls')
                funciones.valorCartas(listajugadores[i],listabanca)
                funciones.verCartas(listajugadores,listajugadores[i][0],listabanca)
                respuesta=funciones.preguntaUnaCartaMas(listajugadores[i][0])
                vecesdoblado=0
                while respuesta==("si" or "SI" or "Si" or "sí" or "SÍ" or "Sí"):
                    while vecesdoblado==0 and listajugadores[i][1]>=(listajugadores[i][2]*2):
                        funciones.apuestaJugadores(listajugadores,i)
                        os.system('cls')
                        vecesdoblado=1
                    
                    funciones.repartirCarta(listajugadores,baraja,i)
                    os.system('cls')
                    funciones.verCartas(listajugadores,listajugadores[i][0],listabanca)
                    pasado=funciones.valorCartas(listajugadores[i],listabanca)
                    
                    if not pasado:
                        respuesta=funciones.preguntaUnaCartaMas(listajugadores[i][0])
                        os.system('cls')
                    if pasado:
                        respuesta="no"
                os.system('cls')
                if i != len(listajugadores)-1:
                    prints.siguiente_jugador()
                    
                    prints.colorinput("Pulsa \"ENTER\" para pasar al siguiente jugador.")
            funciones.valorCartasBanca(listabanca)
            while listabanca[2]<17: #La banca saca cartas hasta que obtiene un valor de 17 o mas
                funciones.repartirCartaBanca(listabanca,baraja)
                funciones.valorCartasBanca(listabanca)
            funciones.compararCartas(listajugadores,listabanca,tasa_normal, tasa_blackjack)
            os.system('cls')
            funciones.verMesa(listajugadores,listabanca)
            funciones.eliminarDatosRonda(listajugadores)
            if listabanca[0]<=0:
                opcion="terminar"
            else:
                del listabanca[1:]
                os.system('cls')
                opcion=funciones.menuJuego(listajugadores) #Menu de cuando finaliza la ronda, se devuelve valor porque si  opcion="terminar" se rompe el bucle y termina la partida
                if len(listajugadores)!=0:
                    primerJugador=listajugadores.pop(0) #El jugador que hablaba primero pasa a hablar el ultimo
                    listajugadores.append(primerJugador)
    opc=funciones.menuPrincipal(listabanca,tasa_normal, tasa_blackjack, numero_barajas)
os.system('cls')
prints.adios()
print("")
prints.colorinput("Pulsa \"ENTER\" para cerrar el programa.")
