# Actualizado 21 de Mayo 2020
# Función funcional
# Convierte un valor entero a binario y agrega una casilla para guardar el valor de verdad
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