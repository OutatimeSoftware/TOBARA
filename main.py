def main():

	# lista de mintérminos.
	fun = [ 0, 1, 2, 3, 4 ];
	# Funcion para capturar los terminos.
	print( getTable( fun ) )

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

	binario.append( 0 )

	return binario

def getTable ( fun ):

	table = [  ]

	var = 3

	tam = y = 2 ** var 

	for i in range( y ):

		table.append( getBin( i, var ) )
	
	for i in fun:
	
		table[i][ var ] = 1

	return table
	
if __name__ == "__main__":

    main()
