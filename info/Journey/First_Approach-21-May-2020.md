# [21 de Mayo del 2020]

## [Revision y ajustes de los avances del proyecto]

Al revisar las funciones que realizamos anteriormente se tuvo que modificar algunas cosas: 

+ Por cuestión de inexperiencia, temporalmente solo intentaremos reducir expresiones de 4 variables o menos. 

+ En cuestión de la implementación, todas las funciones serán reemplazadas para actualizarlas con la nueva implementación, utilizando las nuevas:

    * Temporalmente usaremos dos variables para la captura de datos, var (variables entera con el número de variables de la función) y minTer (una lista que contiene los mintérminos de la función).
    * getTable(variables, minTer): Retorna una matriz con todos los mintérminos de una función.
    * getMinTable(variables, minTer): Retorna una matriz con los mintérminos positivos de una función.
    * getKmap(variables, minTer): Retorna una matriz Kmap con los mintérminos activos de la función.
    * reduceKmap( Kmap ): Encuentra los términos reducibles de un Kmap y retorna una lista de los términos reducidos de la función.

+ Para las pruebas, Se creó una carpeta ( test ) qué contendrá un Markdown de la explicación de las pruebas individuales del código, además de los códigos para probar directamente el código.

+ Temas de aplicaciones: Se creó una carpeta (apps), para comprobar la funcionalidad del código, se plantea una pequeña aplicación para visualizar la reducción de Kmaps con una interfaz hecha en PyGame.

+ En cuestión de la codificación, Para ir probando el código se seguirá usando en la carpeta principal el archivo main.py, luego de comprobar el funcionamiento de las funciones se dividirán en las funciones individuales en Source.

> Nota importante: Las tres primeras funciones ya están listas. 

+ Se realizó la bitácora correspondiente.
