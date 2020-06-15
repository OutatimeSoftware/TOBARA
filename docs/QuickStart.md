# TOBARA Quick Start.

TOBARA es una libreria de python diseñada para la manipulación de algebra booleana que nos facilita la implementación de ciertas herramientas, como las tablas de verdad, los kmaps, etc.
Para comenzar a utilizar TABORA lo único que necesitas entender son los conceptos básicos del algebra booleana para poder representar de manera correcta lo que nosotros podemos observar, por lo que primero intentemos ver como funcionana las partes esenciales: el número de variables y los mintérminos.

Para definir una función booleana nosotros tenemos que definir el número de variables que lo conforman, esto lo puedes saber observas la cantidad de letras involucradas en tu función booleana, por otro lado, los mintérminos son la representación booleana de dichas variables.

Si te pones pensar, existe una relación muy sencila entre las variables y los mintérminos, cada vez que agregas una variable, tienes que contemplar dos posibilidades más de formar un término, pero veamoslo de una manera más visual:


```python
tabla = getTable( 1,[ ] )
print( "1 variable" )
for line in tabla:
    print( line )
print()

tabla = getTable( 2,[ ] )
print( "2 variables" )
for line in tabla:
    print( line )
print()
    
tabla = getTable( 3,[ ] )
print( "3 variables" )
for line in tabla:
    print( line )
print()
    
tabla = getTable( 4,[ ] )
print( "4 variables" )
for line in tabla:
    print( line )
```

    1 variable
    [0, 0]
    [1, 0]
    
    2 variables
    [0, 0, 0]
    [0, 1, 0]
    [0, 1, 0]
    [1, 1, 0]
    
    3 variables
    [0, 0, 0, 0]
    [0, 0, 1, 0]
    [0, 0, 1, 0]
    [0, 1, 1, 0]
    [0, 0, 1, 0]
    [1, 0, 1, 0]
    [0, 1, 1, 0]
    [1, 1, 1, 0]
    
    4 variables
    [0, 0, 0, 0, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 0, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [0, 1, 0, 1, 0]
    [0, 0, 1, 1, 0]
    [0, 1, 1, 1, 0]
    [0, 0, 0, 1, 0]
    [1, 0, 0, 1, 0]
    [0, 1, 0, 1, 0]
    [1, 1, 0, 1, 0]
    [0, 0, 1, 1, 0]
    [1, 0, 1, 1, 0]
    [0, 1, 1, 1, 0]
    [1, 1, 1, 1, 0]
    
