# Actualizado 15 de junio 2020
# Función funcional
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