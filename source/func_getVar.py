def getVar( fun ):
	
	tam = fun
	
	menor = mayor = ord( fun[ 0 ] )
	
	for i in tam :
	
		val = ord( i )
		
		if ( val > mayor and val <= 122 ):
	
			mayor = val
	
		elif ( val < menor and val >= 97 ):
	
			menor = val

	return mayor - menor + 1
