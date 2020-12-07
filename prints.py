def colorreset(): print("\033[92m") 

def colorjugadoractual(): print("\033[96m") 
def colorbanca(): print("\033[95m") 
def colorerror(skk):
    print("\033[91m {}\033[00m" .format(skk))
    colorreset()
def colorinput(skk):
    print("{}" .format(skk), end="\033[33m \n")
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
    print("   ║                       Hola y bienvenidos a su programa de BlackJack preferido!                       ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def empezar():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                       ¡Que empiece la partida!                                       ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def siguiente_jugador():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                  Vale! pasemos al siguiente jugador                                  ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

def mesa():
    banner()
    print("   ╔══════════════════════════════════════════════════════════════════════════════════════════════════════╗")
    print("   ║                                                                                                      ║")
    print("   ║                                          Cartas en la mesa                                           ║")
    print("   ║                                                                                                      ║")
    print("   ╚══════════════════════════════════════════════════════════════════════════════════════════════════════╝")

