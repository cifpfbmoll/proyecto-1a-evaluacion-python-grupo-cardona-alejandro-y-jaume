## Sprint Backlog

Al ser la primera vez que hacemos un proyecto de programación los 3, y además ser la primera vez que hacemos algo con la metodología SCRUM, hemos decidido que en este primer sprint simplemente planificaremos nuestros objetivos a grandes rasgos y decidir las funciones que desarrollaremos cada uno. En primer lugar, decidimos que el sprint dure 2 semanas, donde intentaremos tener la estructura del programa definida y las funciones básicas (la baraja, barajar, repartir cartas, añadir jugadores, apuestas, bucles de partida y ronda, ...) para poder tener así un programa funcional. Nuestro objetivo principal es poder hacer un juego de blackjack con una banca, que será el ordenador, en la que puedan participar un número de personas, 7 o 8 a la vez, sin ningún bug ni fallo y lo más parecido a la realidad (que se pueda apostar, pedir cartas, doblar apuestas antes de pedir cartas, desbancar a la banca, que la banca te desbanque, que la última carta que se ha repartido a cada jugador solo la pueda ver el jugador propietario, como en la realidad, ....). También hemos decidido, aunque puede haber cambios, que utilizaremos listas anidadas para almacenar la información (nombre, dinero, apuesta, ...) de cada jugador y de la banca, bucles para que no se cierre el programa y para simular la partida, sus rondas y los turnos de los jugadores y utilizaremos estructuras de control de flujo para las diferentes condiciones que pueda tener el programa.

En cuanto a las funciones que desarrollara cada uno de nosotros cabe recalcar que aquí hemos decidido dar mucha flexibilidad, es a decir que aunque cada uno de nosotros tenga asignada una función principal los otros también intervendrán en esa función y viceversa. Principalmente hemos dividido las funciones en:

- Karina: desarrollo de la interfaz gráfica y funciones relacionadas.
- Jaume: Funcionamiento y estructura del programa y funciones relacionadas.
- Cardona: Repaso y corrección del programa en general y búsqueda de bugs y errores.


## Lunes, 16 de noviembre. 

Jaume es el Scrum Master hoy. Hemos empezado a planear la aplicación y la variante de blackjack que usaremos. Karina ha preparado un diagrama con las reglas y los pasos que seguirá el programa para así tener más facilidad a la hora de crear el programa. Cardona ha buscado información por internet para el código. Jaume ha empezado a crear código creando la baraja y funciones de barajar y sacar carta entre otras.

## Martes, 17 de noviembre.

Karina es la Scrum Master hoy. Se ha declarado las reglas del juego y los pasos a seguir durante el juego. Se ha creado la carpeta `RULES` donde se ha subido:

 - `RULES/README.md` Archivo donde explica las reglas del juego. Se incluye el diagrama de los pasos de juego y el valor de las cartas.
 - `RULES/cartas.png` Imagen representativa del valor de las cartas.
 - `RULES/diagrama.svg` Diagrama con los pasos del juego.
 - `RULES/diagrama.drawio` Archivo editable para editar el diagrama.

Se ha profundizado en desarrollar las funciones principales y en resolver los problemas de sincronización del equipo con GitHub.

## Martes, 24 de noviembre.

Cardona es el Scrum Master de hoy. Nos hemos reunido y hemos ido puliendo el código del blackjack. Dentro del GitHub se puede apreciar los últimos commits y nuevos pushes como el de las funciones. Seguimos adelante con el juego, discutiendo y juntando las mejores opciones a la hora de hacer código, cada día pensando en ideas nuevas tanto para implementar como para pulir con la finalidad de llegar a nuestro objetivo. Se destaca en el trabajo de hoy las ideas y creaciones de un diccionario y del cambio de puntuación del AS entre 1 o 11 dependiendo de los puntos que lleve el jugador en su baraja (el programa mirará si el jugador puede utilizar los 11 puntos para alcanzar los 21 puntos, en caso de que se pase de 21 el AS pasará a tener un valor de 1 punto dando al jugador la oportunidad de que no pierda instantáneamente y pueda elegir jugar otra carta más).

## Miércoles, 25 de noviembre.

Jaume es el SCRUM master. Cardona no ha podido asistir a clase, pero estamos en contacto a través de Discord. Seguimos desarrollando código. Estamos decidiendo que variante del juego queremos que ejecute el programa y eligiendo que reglas exactas va a tener, ya que según donde consultamos vemos unas u otras. Karina ha ido actualizando el menú del juego, perfeccionando la interfaz visual del programa y mejorando el código para que sea más atractivo y añadiendo funciones para ver as manos de los jugadores y las cartas en mesa. Jaume y Cardona han seguido añadiendo funciones como contar el valor de las cartas, si alguien se pasa que el programa se dé cuenta y le reste las apuestas a su dinero, …

## Lunes, 30 de noviembre.

Karina es la SCRUM master. Se han solucionado algunos errores internos de las funciones. Se ha modificado el formato en el que se enseña los programas añadiendo colores y se ha añadido información visible.

## Revisión de Sprint

El sprint ha ido mejor que lo que habíamos planeado. Además de crear la estructura del programa (bucles y funciones ordenadas para tener un programa funcional) y las funciones básicas, también hemos creado otras funciones adicionales como son: obtener el valor de las cartas de cada jugador(una función que llama a un diccionario donde hemos dado un valor a cada carta), funciones de interfaz gráfica para ver la mesa desde el punto de vista de un jugador (con la última carta de los otros jugadores tapada) o ver la mesa con todas las cartas a la vista además de un menú de juego que se activa al terminar cada ronda (los jugadores pueden salir de la partida, añadir dinero o se pueden añadir nuevos jugadores).

## Sprint Backlog

En el sprint planning, el cual durara 2 semanas al igual que el anterior, lo que nos dejara con el programa terminado a pocos días de la entrega, hemos planteado las funciones que nos faltan, entre ellas se encuentran: La lista con la información de la banca y sus funciones(añadirle sus cartas has que tenga un valor de más de 17, comprobar su valor, comparar el valor de la banca con el de cada jugador y pagar o cobrar según corresponda), la función del valor de los ases(puede ser 1 o 11) y un menú de inicio de partida donde poder cambiar algunos aspectos del juego.

## Martes, 1 de diciembre.

Cardona es el SCRUM master de hoy. Seguimos retocando el programa para que quede lo mejor posible, puliéndolo al máximo para que quede un buen programa, tanto limpio como bonito, además de completo. Se puede destacar el aumento de archivos para que quede mejor estructurado, así como las constantes actualizaciones del código.

## Sábado, 5 de diciembre.

Jaume es el SCRUM master de hoy. Seguimos perfeccionando el programa. Cardona sigue repasando el código y probando el programa en busca de bugs y posibles mejoras. Jaume tiene que crear diferentes funciones para solucionar bugs (repetición del mensaje has perdido y opción terminar cuando solo queda 1 persona), borrar datos de lista jugadores al terminar ronda y crear lista banca y sus funciones. Karina tiene que añadir la interfaz visual de la banca, además tiene que seguir mejorando la parte estética del programa. Todas estas tareas están asignadas para el fin de semana.

## Lunes, 14 de diciembre.

Karina es la SCRUM master de hoy. Se han añadido un menú inicial al ejecutar el programa y las "opciones". Jaume y Cardona han modificado algunas funciones para optimizar el código y solucionado bugs.

# Revisión de Sprint

Hemos logrado terminar todas las funciones propuestas en el sprint backlog. El programa esta funcional y listo para usarse. Se nos han dado más días para realizar la entrega del proyecto así que aprovecharemos para pasar a función la mayor parte de código posible, reduciendo así el tamaño del programa, y comprobaremos el funcionamiento del programa para que no se nos pase ningún error de comportamiento y que cada parte del código haga lo que le toque hacer.

## Martes, 15 de diciembre.

Cardona es el SCRUM master de hoy. Entre todos se ha ido simplificando y retocando el código habiendo así por ejemplo cambios en el menú y en alguna de las funciones. Se han corregido todos los bugs y fallos encontrados por el momento. El proyecto sigue su curso como queremos (implementando nuevas ideas que van surgiendo) y cada día trabajamos para pulirlo un poco más, repito, con cambios y actualizaciones y corrigiendo los errores.

## Miércoles, 16 de diciembre.

Jaume es el Scrum master de hoy. Hemos estado comprobando que el código funcionara bien y no tuviera fallos. Karina ha estado creando diversas funciones del menú inicial del juego y optimizando diversas líneas de código. Cardona y yo nos hemos centrado en comprobar que todo funcionara como toca.
