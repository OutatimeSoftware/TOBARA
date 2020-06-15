'''
Fuente teorica y base: Scientia et Technica Año XIII, No x, Mes de 200x. Universidad Tecnológica de Pereira. ISSN 0122-1701
Referencia en código: https://repl.it/talk/learn/Python-Quine-McCluskey-Algorithm/14461
                      

Funcionamiento del algoritmo
1. Busqueda de implicantes primos
2. Hacer tabla de implicantes primos
3. Encontrar tabla de implicantes primos
'''

# Comparar dos strings buscando si tienen un valor en común
# Devuelve la posición del valor diferente.
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

#Compara si el numero es igual a un implicante 
#Devuelve un valor de verdad

def compBinarySame( term, number ):
    
    for i in range( len( term ) ):
    
        if term[ i ] != '-':
    
            if term[ i ] != number[ i ]:
    
                return False

    return True

# Comprueba si hay parejas con elementos reducibles y crea un nuevo grupo
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

# Descarta listas repetidas en la tabla
def removeRedundant( group ):

    newGroup = [ ]
    
    for j in group:
    
        new=[ ]
    
        for i in j:
    
            if i not in new:
    
                new.append( i )
    
        newGroup.append( new )
    
    return newGroup

# Función de comprobación para grupos vacios
# Retorna un valor booleano en respuesta 
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

# Cambiar de binario a letra
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
