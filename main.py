def main():
	
	funcion = input()

	# Funcion para capturar los terminos.
	
	getFun( funcion )
	
	print( getTable(  ) )

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

	# Quita esto flojo o cambialo xd

	binario.append( 0 )

	return binario

def getTable (  ):

	table = [  ]

	var = 3

	tam = y = 2 ** var 

	for i in range( y ):

		table.append( getBin( i, var ) )

	return table
	
if __name__ == "__main__":

    main()
