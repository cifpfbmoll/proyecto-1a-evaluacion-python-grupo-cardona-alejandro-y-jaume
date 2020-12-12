## Sprint Backlog

Al ser la primera vez que hacemos un proyecto de programación los 3, y además ser la primera vez que hacemos algo con la metodología SCRUM, hemos decidido simplemente planificar nuestros objetivos a grandes rasgos y decidir las funciones que desarrollaremos cada uno. En primer lugar, decidimos que el sprint dure hasta 1 semana antes de la entrega del proyecto, donde intentaremos tener el proyecto funcional y terminado con las capacidades que hemos considerado esénciales. La ultima semana intentaremos hacer otro sprint mas corto para añadir funciones extras que nos parezcan interesantes para mejorar el programa. Nuestro objetivo principal es poder hacer un juego de blackjack con una banca, que será el ordenador, en la que puedan participar un numero de personas, 7 o 8 a la vez, sin ningún bug ni fallo i lo mas parecido a la realidad. En cuanto a las funciones que desarrollara cada uno de nosotros cabe recalcar que aquí hemos decidido dar mucha flexibilidad, es a decir que aunque cada uno de nosotros tenga asignada una función principal los otros también intervendrán en esa función i viceversa. Principalmente hemos dividido las funciones en: 

- Karina: desarrollo de la interfaz grafica y funciones relacionadas.
- Jaume: Funcionamiento y estructura del programa y funciones relacionadas.
- Cardona: Repaso y corrección del programa en general y búsqueda de bugs y errores.


## Lunes, 16 de noviembre. 

Jaume es el Scrum Master hoy. Hemos empezado a planear la aplicación y la variante que usaremos. Karina ha preparado un diagrama con las reglas i los pasos que seguirá el programa para así tener mas facilidad a la hora de crear el programa. Cardona ha buscado información por internet para el código. Jaume ha empezado a crear código creando la baraja i funciones de barajar i sacar carta entre otras.

## Martes, 17 de noviembre.

Karina es la Scrum Master hoy. Se ha declarado las reglas del juego y los pasos a seguir durante el juego. Se ha creado la carpeta `RULES` donde se ha subido:

 - `RULES/README.md` Archivo donde explica las reglas del juego. Se incluye el diagrama de los pasos de juego y el valor de las cartas.
 - `RULES/cartas.png` Imagen representativa del valor de las cartas.
 - `RULES/diagrama.svg` Diagrama con los pasos del juego.
 - `RULES/diagrama.drawio` Archivo editable para editar el diagrama.

Se ha profundizado en desarrollar las funciones principales y en resolver los problemas de sincronización del equipo con Github.

## Martes, 24 de noviembre.

Cardona es el Scrum Master de hoy. Nos hemos reunido y hemos ido puliendo el código del blackjack. Dentro del github se puede apreciar los últimos commits y nuevos pushes como el de las funciones. Seguimos adelante con el juego, discutiendo y juntando las mejores opciones a la hora de hacer código, cada día pensando en ideas nuevas tanto para implementar como para pulir con la finalidad de llegar a nuestro objetivo. Se destaca en el trabajo de hoy las ideas y creaciones de un diccionario y del cambio de puntuación del AS entre 1 o 11 dependiendo de los puntos que lleve el jugador en su baraja (el programa mirará si el jugador puede utilizar los 11 puntos para alcanzar los 21 puntos, en caso de que se pase de 21 el AS pasará a tener un valor de 1 punto dando al jugador la oportunidad de que no pierda instantáneamente y pueda elegir jugar otra carta más).

## Miércoles, 25 de noviembre.

Jaume es el SCRUM master. Cardona no ha podido asistir a clase, pero estamos en contacto a través de discord. Seguimos desarrollando código. Estamos decidiendo que variante del juego queremos que ejecute el programa i eligiendo que reglas exactas va a tener, ya que según donde consultamos vemos unas o otras. Karina ha ido actualizando el menú del juego, perfeccionando la interfaz visual del programa y mejorando el código para que sea mas atractivo y añadiendo funciones para ver as manos de los jugadores y las cartas en mesa. Jaume y Cardona han seguido añadiendo funciones como contar el valor de las cartas, si alguien se pasa que el programa se de cuenta i le reste las apuestas a su dinero,…

## Lunes, 30 de noviembre.

Karina es la SCRUM master. Se han solucionado algunos errores internos de las funciones. Se ha modificado el formato en el que se enseña los programas añadiendo colores y se ha añadido información visible.

## Martes, 1 de diciembre.

Cardona es el SCRUM master de hoy. Seguimos retocando el programa para que quede lo mejor posible, puliendolo al máximo para que quede un buen programa, tanto limpio como bonito, además de completo. Se puede destacar el aumento de archivos para que quede mejor estructurado, así como las constantes actualizaciones del código.

## Sabado, 5 de diciembre.

Jaume es el SCRUM master de hoy. Seguimos perfeccionando el programa. Cardona sigue repasando el código i probando el programa en busca de bugs i posibles mejoras. Jaume tiene que crear diferentes funciones para solucionar bugs (repetición del mensaje has perdido i opción terminar cuando solo queda 1 persona), borrar datos de lista jugadores al terminar ronda i crear lista banca i sus funciones. Karina tiene que añadir la interfaz visual de la banca, además tiene que seguir mejorando la parte estética del programa. Todas estas tareas están asignadas para el fin de semana.