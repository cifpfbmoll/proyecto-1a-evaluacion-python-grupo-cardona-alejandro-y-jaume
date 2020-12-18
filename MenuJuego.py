import os
import funciones
import prints
import objetos
listabanca=[1000000]

apuesta_normal = 1 
apuesta_blackjack = 2
numero_barajas = 8
#Optimizar funciones.
opc,apuesta_normal,apuesta_blackjack,numero_barajas = funciones.menuPrincipal(listabanca, apuesta_normal, apuesta_blackjack, numero_barajas)
while opc != "4":
    if opc == "3":
        if listabanca[0]==0:
            funciones.dineroBanca(listabanca)
        numerojugadores=prints.colorinput("Cuantos jugadores vais a entrar? [1-7]")
        while numerojugadores not in ["1","2","3","4","5","6","7"]:
            os.system('cls')
            prints.creando()
            prints.colorerror("\n    ⚠  Has de seleccionar un número del 1 al 7.")
            numerojugadores=prints.colorinput("Cuantos jugadores vais a entrar? [1-7]")
        os.system('cls')
        prints.creando()
        listajugadores=funciones.nombreJugadores(int(numerojugadores))
        os.system('cls')
        prints.creando()
        print("   >>> Con cuanto dinero vais a entrar cada uno?\n")
        funciones.dineroJugadores(listajugadores)
        os.system('cls')
        prints.creando()
        opcion=""
        while opcion!="terminar":
            os.system('cls')
            prints.empezar()
            print ("   >>> Hagan sus apuestas!\n")
            funciones.apuestaInicialJugadores(listajugadores)
            baraja=funciones.barajar(objetos.baraja[:]*numero_barajas)
            funciones.repartirCartasIniciales(listajugadores,baraja)
            funciones.repartirCartaBanca(listabanca,baraja)
            funciones.repartirCartasIniciales(listajugadores,baraja)
            for i in range (len(listajugadores)):
                os.system('cls')
                funciones.valorCartas(listajugadores[i],listabanca)
                funciones.verCartas(listajugadores,listajugadores[i][0],listabanca)
                respuesta=prints.colorinput(f"Quieres una carta mas {listajugadores[i][0]}?  [ si /NO ]")
                while respuesta not in ["si","no","SI","NO","Si","No","sí","SÍ","Sí",""]:
                    prints.colorerror("    ⚠  Porfavor escriba si o no")
                    respuesta=prints.colorinput(f"Quieres una carta mas {listajugadores[i][0]}?  [ si / NO ]")
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
                        respuesta=prints.colorinput("Quieres una carta mas? [ si / NO ]")
                        while respuesta not in ["si","no","SI","NO","Si","No","sí","SÍ","Sí",""]:
                            prints.colorerror("    ⚠  Porfavor escriba si o no")
                            respuesta=prints.colorinput("Quieres una carta mas? [ si / NO ]")
                        os.system('cls')
                    if pasado:
                        respuesta="no" or "NO" or "No"
                os.system('cls')
                if i != len(listajugadores)-1:
                    prints.siguiente_jugador()
                    
                    prints.colorinput("Pulsa \"ENTER\" para pasar al siguiente jugador.")
            funciones.valorCartasBanca(listabanca)
            while listabanca[2]<17: #La banca saca cartas hasta que obtiene un valor de 17 o mas
                funciones.repartirCartaBanca(listabanca,baraja)
                funciones.valorCartasBanca(listabanca)
            funciones.compararCartas(listajugadores,listabanca,apuesta_normal, apuesta_blackjack)
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
    opc=funciones.menuPrincipal(listabanca,apuesta_normal, apuesta_blackjack, numero_barajas)
os.system('cls')
prints.adios()
print("")
prints.colorinput("Pulsa \"ENTER\" para cerrar el programa.")
