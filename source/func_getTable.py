# Actualizado 21 de Mayo 2020
# Función funcional
def getTable ( var, fun ):

	table = [  ]

	tam = y = 2 ** var 

	for i in range( y ):

		table.append( getBin( i, var ) )
	
	for i in fun:
	
		table[i][ var ] = 1

	return table
