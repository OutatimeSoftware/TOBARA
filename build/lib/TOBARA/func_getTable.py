# Actualizado 21 de Mayo 2020
# Función funcional
from func_getBin import *

def getTable ( var, fun ):

	table = [  ]

	tam = y = 2 ** var 

	for index in range( y ):

		table.append( getBin( index, var ) )
	
	for minTer in fun:
	
		table[ minTer ][ var ] = 1

	return table
