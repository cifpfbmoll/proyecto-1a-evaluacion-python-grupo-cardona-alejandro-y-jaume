def valorcartas (listajugadores,listabanca):
    valormano=0
    apuesta=listajugadores[2]
    for i in listajugadores[3]:
        valormano+=objetos.valor_baraja.get(i)
    while valormano>21:
        
    if valormano>21:
        if listajugadores[-1]==listajugadores[3]:
            listajugadores.append(valormano)
            print ("   >>> Looseeeeer!")
            print ("   >>> Tu puntuación es mayor a 21.")
            dinerojugador=(listajugadores.pop(1))-apuesta
            listajugadores.insert(1,dinerojugador)
            dinerobanca=listabanca.pop(0)+apuesta
            listabanca.insert(0,dinerobanca)
            pasado=True
            prints.colorinput("\n   >>> Pulsa ENTER para abandonar la mesa.")
        else:
            del listajugadores[4]
            listajugadores.append(valormano)
            print ("   >>> Looseeeeer!")
            print ("   >>> Tu puntuación es mayor a 21.")
            dinerojugador=(listajugadores.pop(1))-apuesta
            listajugadores.insert(1,dinerojugador)
            dinerobanca=listabanca.pop(0)+apuesta
            listabanca.insert(0,dinerobanca)
            pasado=True
            prints.colorinput("\n   >>> Pulsa ENTER para abandonar la mesa.")
    else:
        if listajugadores[-1]==listajugadores[3]:
            listajugadores.append(valormano)
            pasado=False
        else:
            del listajugadores[4]
            listajugadores.append(valormano)
            pasado=False

    return pasado