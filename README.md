# projectTOBARA

The Only Boolean Algebra Reduction App

## Descripción

Nuestro sistema es una herramienta de análisis de funciones booleanas, cuya tarea principal es reducir lo máximo posible una función booleana.
Con estos datos realizaremos una API que permita a cualquier usuario consultar estos elementos de cualquier función booleana que quieran introducir.

## Proceso

Nuestro sistema tendrá como objetivo principal el análisis de funciones booleanas y su descomposición en sus componentes principales:
    • Recibir la función
    • Determinar sus variables 
    • Determinar sus terminos
    • Reducción de la función

## Objetivo

Algoritmos de reducción de funciones booleanas. 

## Requerimientos

##### Actores del sistema

Usuario. Persona que usa el sistema.

- Puede consultar si una expresión booleana se encuentra en su expresión mínima (no se puede reducir más).

- Puede ingresar una función booleana para ser reducida a su expresión mínima.

- Puede recibir su función booleana en su expresión de suma de productos.

##### Requerimientos del usuario

- Los usuarios podrán preguntar si una función se encuentra en su expresión mínima.

- Los usuarios podrán ingresar una función booleana y obtendrán su expresión mínima.

- Los usuarios podrán convertir su función booleana en su forma de suma de productos.

##### Requerimientos del sistema (funcionales)

1. RF001 (Alta). El sistema deberá ser capaz de recibir y determinar el numero de variables que tiene la función

2. RF002 (Alta). El sistema deberá ser capaz de recibir y verificar el número de términos que tiene la función

3. RF003 (Alta). El sistema deberá ser capaz de recibir una función booleana y leer sus minterminos implicados

4. RF004 (Alta). El sistema deberá ser capaz de recibir una función booleana y convertirla su expresión de suma de productos.

5. RF005 (alta). El sistema deberá ser capaz de reducir la función hasta su mínima expresión
