# Documentación
Nuestras funciones se definen en dos grandes partes: Las funciones de usuario y las funciones internas.


## Funciones internas.
### getBin.


```python
def getBin ( val, var ):

    binario = [  ]

    for cell in bin( val )[ 2: ]:
        
        binario.append( int( cell ) )

    tam = len( binario )

    for i in range( var - tam ):
    
        binario.append( 0 )
        
    binario.reverse(  )

    binario.append( 0 )

    return binario
```

Convierte un valor entero a binario.
* Entrada: Un valor entero y el número de variables.
* Proceso: Vuelve el valor entero a su representación binaria, acompleta los espacios faltantes y agrega una casilla para guardar el valor de verdad de término.
* Salida: Una lista de valores booleanos que representan un término de la función booleana.

### binaryToLetter.


```python
def binaryToLetter( s ):

    result = ''
    
    c = 'a'
    
    n = 0
    
    for i in range(len(s)):
       
        if s[i] == '1':

            result = result + c

        elif s[i] == '0':

            result = result + c+'\''

        n += 1

        c = chr( ord( c ) + 1 )
    
    return result
```

Transforma los valores de un término binario en su respectiva representación literal.
* Entrada: Un término de la función booleana.
* Proceso: Convierte los los valores booleanos del término en su respectiva representación literal de la a-z.
* Salida: Un arreglo que representa la expresión literal del término booleano.

### compBinary.


```python
def compBinary( s1, s2 ):

    cont = 0
    
    position = 0

    for pos in range( len( s1 ) ):

        if( s1[ pos ] != s2[ pos ] ):

            cont += 1

            position = pos

    if( cont == 1 ):

        return True, position

    else:

        return False, None
```

Compara dos términos booleanos buscando si tienen un valor en común.
* Entrada: Dos términos booleanos del mismo tamaño.
* Proceso: Para este caso particular solo nos interesa si tienen una sola similitud, en los casos contrarios, se considera que no se puede reducir.
* Salida: Devuelve la posición del valor diferente.

### compBinarySame


```python
def compBinarySame( term, number ):
    
    for i in range( len( term ) ):
    
        if term[ i ] != '-':
    
            if term[ i ] != number[ i ]:
    
                return False

    return True
```

Compara si el numero es igual a un implicante primo.
* Entrada: Un término y un número.
* Proceso. Recorre ambos arreglos buscando diferencias. 
* Salida: Devuelve un valor de verdad.

### combinePairs


```python
def combinePairs( group, result ):
    # Define el tamaño del grupo
    size = len( group ) -1

    # Inicializa lista para verificar comprobación
    check = [ ]

    # Crea el nuevo grupo de terminos
    nextGroup = [ [ ] for x in range( size )]

    # Comprueba cada elemento del grupo comparandolo con el siguiente
    for i in range( size ):

        for element in group[ i ]:

            for element2 in group[ i + 1 ]:

                checkEqual, pos = compBinary( element, element2 )

                if ( checkEqual == True ):

                    # Actualización de la lista de verificación
                    check.append( element )
                    
                    check.append( element2 )
                    
                    #Anula los valores simplificables con un ( "-" )
                    newElement = list( element )
                    
                    newElement [ pos ] = '-'
                    
                    newElement = "".join( newElement )
                    
                    nextGroup[ i ].append( newElement )

    for i in group:

        for j in i:

            if j not in check:

                result.append(j)

    return nextGroup, result
```

Comprueba si hay parejas entre dos grupos
* Entrada: Un grupo de mintérminos con el mismo número de elementos de verdad y una lista de implicantes primos.
* Proceso: Comprueba si hay parejas con elementos reducibles y crea un nuevo grupo para las parejas reducidas.
* Salida: Una lista de términos reducidos.

### removeRedundant


```python
def removeRedundant( group ):

    newGroup = [ ]
    
    for j in group:
    
        new=[ ]
    
        for i in j:
    
            if i not in new:
    
                new.append( i )
    
        newGroup.append( new )
    
    return newGroup
```

Elimina términos repetidos de un grupo
* Entrada: Una lista de términos con el mismo número de elementos de verdad.
* Proceso: Compara los elementos que no existan en una nueva lista y los guarda para eliminar posibles términos repetidos.
* Salida: Una lista de términos sin repetición.

### checkEmpty


```python
def checkEmpty(group):

    if len( group ) == 0:

        return True

    else:

        cont = 0
        
        for i in group:
        
            if i:
        
                cont+=1
        
        if ( cont == 0 ):
        
            return True
    
    return False
```

Verifica si un grupo esta sin términos.
* Entrada: Una lista de términos con el mismo número de elementos de verdad.
* Proceso: Comprueba si la lista se encuentra sin elementos
* Salida: Un valor booleano que responde a la pregunta.

## De Usuario

### getTable


```python
def getTable ( var, fun ):

    table = [  ]

    tam = y = 2 ** var 

    for index in range( y ):

        table.append( getBin( index, var ) )
    
    for minTer in fun:

        table[ minTer ][ var ] = 1

    return table
```

Genera una matriz que representa una tabla de verdad.
* Entrada: El número de variables de la función booleana y una lista con los mintérminos de le expresión.
* Proceso: Transforma los indices de la tabla y agrega su respectivo valor de verdad.
* Salida. Una matriz que representa la tabla de verdad de la función booleana introducida.

### getMinTable


```python
def getMinTable ( var, fun ):

    table = [  ]

    pos = 0

    for i in fun:

        table.append( getBin( i, var ) )

        table[ pos ][ var ] = 1

        pos += 1

    return table
```

Genera una matriz que representa una tabla de verdad.
* Entrada: El número de variables de la función booleana y una lista con los mintérminos de le expresión.
* Proceso: Transforma los indices de la tabla y unicamente agregando a los elementos que tengan un valor de verdadero.
* Salida. Una matriz que representa la tabla de verdad de la función booleana introducida excluyendo a los términos con valor negativo.

### getKmap


```python
def getKmap( var, fun ):

    Kmap = [  ]

    for i in range( var ):

        Kmap.append( [ ] )

        for j in range( var ):

            Kmap[ i ].append( 0 )

    for minTer in fun:

        x = ( minTer ) // var
        
        y = ( minTer ) % var

        Kmap[ y ][ x ] = 1

    return Kmap
```

Genera una matriz que representa un Kmap
* Entrada: El número de variables de la función booleana y una lista con los mintérminos de le expresión.
* Proceso: Transforma el valor de los indices del mintérmino en las coordenadas generales de los kmaps.
* Salida. Una matriz que representa el kmap de la función booleana.

### reduceFun


```python
def reduceFun( n, fun ):  

    # transformación de lista en enteros
    fun = list( map( int, fun ) )

    # Crea la lista inicial
    group = [ [ ] for x in range ( n + 1 )]

    for i in range( len( fun )):

        # Conversor a binario
        fun[ i ] = bin( fun[ i ] )[ 2: ]

        if len( fun[ i ] ) < n:
            # Completar el término con ceros
            for j in range( n - len( fun[ i ] ) ):
                fun[ i ] = '0' + fun[ i ]
       
        # grupos de 1
        index = fun[ i ].count( '1' )

        # Sub grupos
        group[ index ].append( fun[ i ])


    allGroup = [ ]

    result = [ ]
    
    # Combinar las parejas que no han sido conbinadas
    while checkEmpty( group ) == False:

        allGroup.append( group )
        
        nextGroup, result = combinePairs( group, result )
        
        group = removeRedundant( nextGroup )

    s = ""

    for i in result:

        s = s + binaryToLetter( i ) + " + "

    # - 3 para eliminar el " + " extra 
    return s[ :( len( s ) - 3 ) ]
```

Función que sirve para encontrar implicantes primos de una expresión booleana y reducirlos.
* Entrada: El número de variables de la función booleana y una lista con los mintérminos de le expresión.
* Proceso: Crea los grupos de términos con el mismo número de valores de verdad y los compara para buscar expresiones reducibles.
* Salida: Un string de elementos que representan la expresión minimizada 
