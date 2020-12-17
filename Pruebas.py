lista=["jugador","sudinero","apuesta",["cartasenMano"],"valormano"]

listabanca=["Dinero",["cartas"],"valorcartas"]

import prints

prints.adios()

count=0

for i in listabanca:

    count+=i.count("carta")



print (count," ",listabanca.count("cartas"))
