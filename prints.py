def colorreset(): print("\033[92m") 

def colorjugadoractual(): print("\033[96m") 
def colorbanca(): print("\033[95m") 
def colorganador(): print("\033[93m") 
def colorperdedor(): print("\033[91m") 
def colorerror(skk):
    print("\033[91m {}\033[00m" .format(skk))
    colorreset()
def colorinput(skk):
    print("\033[33m   >>> \033[92m%s" % (skk), end="\033[33m \n")
    valor = input("    >  ")
    colorreset()
    return valor

def banner():
    colorreset()
    print("           ______                                         __                                            ")
    print("          //   ) )                                       / /                               ___     ____ ")
    print("         //___/ /  //  ___      ___     / ___           / /  ___      ___     / ___      //   ) ) /_  / ")
    print("        / __  (   // //   ) ) //   ) ) //\ \           / / //   ) ) //   ) ) //\ \        ___/ /   / /  ") 
    print("       //    ) ) // //   / / //       //  \ \         / / //   / / //       //  \ \     / ____/   / /   ")   
    print("      //____/ / // ((___( ( ((____   //    \ \  ((___/ / ((___( ( ((____   //    \ \   / /____   / /    ")
    print("   ")

def inicio():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                          Bienvenido/s a su programa de BlackJack preferido!                          ║")
    print("   ║                                                                                                      ║")
    print("   ╠═════════════════════════════════════════╦══════════════════╦═════════════════════════════════════════╣")
    print("   ╠═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═╣  Menú principal  ╠═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═╣")
    print("   ╚═════════════════════════════════════════╩══════════════════╩═════════════════════════════════════════╝")
    print("")
    print("     1 >> Opciones")
    print("     2 >> Ver reglas")
    print("     3 >> Empezar partida")
    print("     4 >> Salir")
    print("")


def opciones(dinerobanca):
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                          Bienvenido/s a su programa de BlackJack preferido!                          ║")
    print("   ║                                                                                                      ║")
    print("   ╠═════════════════════════════════════════╦══════════════════╦═════════════════════════════════════════╣")
    print("   ╠═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═╣     Opciones     ╠═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═╣")
    print("   ╚═════════════════════════════════════════╩══════════════════╩═════════════════════════════════════════╝")
    print("")
    print("     1 >> Dinero inicial de la banca. [ Actual: %d ]" % (dinerobanca))
    print("     2 << Volver atrás")
    print("")

def reglas():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                          Bienvenido/s a su programa de BlackJack preferido!                          ║")
    print("   ║                                                                                                      ║")
    print("   ╠═════════════════════════════════════════╦══════════════════╦═════════════════════════════════════════╣")
    print("   ╠═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═╣      Reglas      ╠═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═ ═╣")
    print("   ╚═════════════════════════════════════════╩══════════════════╩═════════════════════════════════════════╝")
    print("")
    print("     1 >> Objetivo: superar a la banca en puntuación sin pasar de 21.")
    print("     2 >> J, Q y K suman 10 puntos.")
    print("     3 >> Un AS puede sumar 11 o 1.")
    print("     4 >> Se considera BlackJack tener 21 puntos con una combinación de 2 cartas.")
    print("     5 >> Todos los jugadores juegan contra la banca, sin embargo tendrán una carta oculta.")
    print("     6 >> La banca sacará cartas para si misma hasta que tenga una puntuación de 17 o superior.")
    print("")
    colorinput("Pulsa \"ENTER\" para volver al menú.")

def empezar():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                       ¡Que empiece la partida!                                       ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def creando():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                          Creando partida...                                          ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def siguiente_jugador():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                ¡Vale! Pasemos al siguiente jugador...                                ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def mesa():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                          Cartas en la mesa                                           ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def menu():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                                 MENÚ                                                 ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def adios():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                          ¡Gracias por jugar!                                         ║")
    print("   ║                                            ¡Hasta pronto!                                            ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")
    print("\n   >>> Creado por...\n\n      >> Karina Carrascosa\n      >> Jaume Fullana\n      >> Jose Luis Cardona")