import os
import funciones
import prints
import objetos

listabanca=[1000000] #Lista con la informacion de la banca, el valor que ya esta dado es el dinero con el que empieza la banca por defecto.
tasa_normal = 1 #numero predeterminado por el que se multiplica la apuesta cuando se gana a la banca sin blackjack.
tasa_blackjack = 2 #numero predeterminado por el que se multiplica la apuesta cuando se gana a la banca teniendo blackjack.
numero_barajas = 8 #numero predeterminado de barajas con las que se juega.

opc,tasa_normal,tasa_blackjack,numero_barajas = funciones.menuPrincipal(listabanca, tasa_normal, tasa_blackjack, numero_barajas) 
while opc != "4":#Bucle que se repite hasta que se desea salir del programa.
    if opc == "3":
        if listabanca[0]==0:#Bucle que solo se activa cuando la partida anterior(no ronda) ha terminado con la banca perdiendo todo su dinero 
            #pero los jugadores han querido seguir jugando, y por tanto no han salido del programa.
            funciones.dineroBanca(listabanca) 
        numerojugadores=funciones.cantidadJugadores()
        funciones.limpiarTerminal()
        prints.creando()
        listajugadores=funciones.nombreJugadores(int(numerojugadores))
        funciones.limpiarTerminal()
        prints.creando()
        funciones.dineroJugadores(listajugadores)
        funciones.limpiarTerminal()
        prints.creando()
        opcion=""
        while opcion!="terminar":#Bucle de las rondas de la partida.
            funciones.limpiarTerminal()
            prints.empezar()
            funciones.apuestaInicialJugadores(listajugadores)
            baraja=funciones.barajar(objetos.baraja[:]*numero_barajas)
            funciones.repartirCartasIniciales(listajugadores,baraja)
            funciones.repartirCartaBanca(listabanca,baraja)
            funciones.repartirCartasIniciales(listajugadores,baraja)
            for i in range (len(listajugadores)):#turnos de los jugadores, cada valor de i es un turno.
                funciones.limpiarTerminal()
                funciones.valorCartas(listajugadores[i],listabanca)
                funciones.verCartas(listajugadores,listajugadores[i][0],listabanca)
                respuesta=funciones.preguntaUnaCartaMas(listajugadores[i][0])
                vecesdoblado=0
                while respuesta==("si" or "SI" or "Si" or "sí" or "SÍ" or "Sí"):
                    if vecesdoblado==0 and listajugadores[i][1]>=(listajugadores[i][2]*2):#Si el jugador quiere una carta mas, no ha
                        #doblado antes i tiene suficiente dinero se entrara en la funcion donde se le pedira si quiere doblar la apuesta
                        funciones.apuestaJugadores(listajugadores,i)
                        funciones.limpiarTerminal()
                        vecesdoblado=1
                    
                    funciones.repartirCarta(listajugadores,baraja,i)
                    funciones.limpiarTerminal()
                    funciones.verCartas(listajugadores,listajugadores[i][0],listabanca)
                    pasado=funciones.valorCartas(listajugadores[i],listabanca)
                    
                    if not pasado:
                        respuesta=funciones.preguntaUnaCartaMas(listajugadores[i][0])
                        funciones.limpiarTerminal()
                    if pasado:
                        respuesta="no"
                funciones.limpiarTerminal()
                if i != len(listajugadores)-1:#Si no es el ultimo jugador se entrar en este bucle para que se haga el siguiente print
                    prints.siguiente_jugador()
                    
                    prints.colorinput("Pulsa \"ENTER\" para pasar al siguiente jugador.")
            funciones.valorCartasBanca(listabanca)
            while listabanca[2]<17: #La banca saca cartas hasta que obtiene un valor de 17 o mas
                funciones.repartirCartaBanca(listabanca,baraja)
                funciones.valorCartasBanca(listabanca)
            funciones.compararCartas(listajugadores,listabanca,tasa_normal, tasa_blackjack)
            funciones.limpiarTerminal()
            funciones.verMesa(listajugadores,listabanca)
            funciones.eliminarDatosRonda(listajugadores)
            if listabanca[0]<=0: #Si la banca se queda sin dinero, se da opcion terminar para que se rompa el bucle de la partida
                opcion="terminar"
            else:
                del listabanca[1:]
                funciones.limpiarTerminal()
                opcion=funciones.menuJuego(listajugadores) #Menu de cuando finaliza la ronda, se devuelve valor porque si  opcion="terminar"
                # se rompe el bucle y termina la partida
                if len(listajugadores)!=0:
                    primerJugador=listajugadores.pop(0) 
                    listajugadores.append(primerJugador)#El jugador que hablaba primero pasa a hablar el ultimo
    opc,tasa_normal,tasa_blackjack,numero_barajas=funciones.menuPrincipal(listabanca,tasa_normal, tasa_blackjack, numero_barajas)
funciones.limpiarTerminal()
prints.adios()
print("")
prints.colorinput("Pulsa \"ENTER\" para cerrar el programa.")