# Documentation
Our functions defines itself in two: User functions and intern functions.

## Intern functions.
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
Converts a binary value to an int value.
* Input: An int and the number of variables.
* Process: Returns the int value into his binary representation, fills the missing spaces and adds a cell to store the truth value. 
* Output: A list of boolean values that represent a term of the boolean function.

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

Transform the values of a binary term in its literal representation.
* Input: A term of the boolean function
* Pocess: Converts the boolean values of the term in its literal 'a-z' representation.
* Output: An array that represents the literal expression of the boolean term.

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

Compare two boolean terms, searching if theres any common value.
* Input: Two boolean terms of the same size
* Process: For this particular case, it is only relevant if they have only one similarity, in other cases, it is considererd that you cannot reduce it.
* Output: Returns the different value position.

### compBinarySame


```python
def compBinarySame( term, number ):
    
    for i in range( len( term ) ):
    
        if term[ i ] != '-':
    
            if term[ i ] != number[ i ]:
    
                return False

    return True
```

Compare if the number is equal to a prime.
* Input: A number and a term
* Process: Walk through both arrays searching differences
* Output: Returns a truth value

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

Prove if there's pairs between two groups.
* Input: A min-term group with the same number of truth elements and a list of primes
* Process: Tests if there are pairs with reducible elements and it creates a new group for the reduced pairs
* Output: A reduced-terms list

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

Remove repeated terms of a group
* Input: A list of terms with the same number of truth elements
* Process: Compare the elements that doesn't exist in a new list and save them to be able to remove possible repeated terms
* Output: A non-repeated term list

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

Checks if there's a terms-less group
* Input: A terms list with the same number of truth elements
* Process: Tests if it is a terms-less list
* Output: A boolean value that answer the initial question

## Of User

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
Generates a matrix that represents a truth table
* Input: The number of varaibles of the boolean function and a list with the min-tems of the expression
* Process: It transform the indexes of the table and it adds their respective truth value
* Output: A matrix that represent the truth table of the introducen boolean function

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
Generates a matrix that represent a truth table
* Input: The number of variables of the boolean function and a list with the min-terms of the expression
* Process: It transform the indexes of the table adding only truthy values
* Output: A matrix that represent the truth table of the introduced boolean function, excluding the non-truthy values.

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

Generates a matrix that represents a Kmap
* Input: The number of variables of the boolean function and a list with the min-terms of the expression
* Process: It transforms the indexes values of the min-terms in the general coordinates of the Kmaps
* Output: A matrix that represents the Kmap of the boolean function

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

Function that it's use it to find primes of an boolean expression to minify them
* Input: The number of variables of the boolean function and a list of the min-terms of the expression
* Process: It creates groups of terms with the same number of truth values and it compares them to search reducible expressions.
* Output: A string of elements that represents the minified expression