def colorreset(): print("\033[92m") 

def colorjugadoractual(): print("\033[96m") 
def colorerror(skk):
    print("\033[91m {}\033[00m" .format(skk))
    colorreset()
def colorinput(skk):
    print("{}" .format(skk), end="\033[33m \n")
    valor = input(" >  ")
    colorreset()
    return valor

def inicio():
    print ("╔════════════════════════════════════════════════════════════════════╗")
    print ("║                                                                    ║")
    print ("║      Hola y bienvenidos a su programa de BlackJack preferido!      ║")
    print ("║                                                                    ║")
    print ("╚════════════════════════════════════════════════════════════════════╝")

def empezar():
    print("╔════════════════════════════════════════════════════════════════════════╗")
    print("║                                                                        ║")
    print("║                        ¡Que empiece la partida!                        ║")
    print("║                                                                        ║")
    print("╚════════════════════════════════════════════════════════════════════════╝")

def siguiente_jugador():
    print("╔════════════════════════════════════════════════════════════════════╗")
    print("║                                                                    ║")
    print("║                 Vale! pasemos al siguiente jugador                 ║")
    print("║                                                                    ║")
    print("╚════════════════════════════════════════════════════════════════════╝")