def getBin ( val, var ):

	binario = [  ]

	check = True

	while ( val != 1 and val != 0 ):

		binario.append( val % 2 )

		val = val // 2

	binario.append( val % 2 )

	tam = len( binario )

	for i in range( var - tam ):
	
		binario.append( 0 )

	binario.reverse(  )

	return binario
