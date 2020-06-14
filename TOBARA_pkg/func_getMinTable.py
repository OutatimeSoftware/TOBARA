# Actualizado 22 de Mayo 2020
# Función funcional
from func_getBin import *

def getMinTable ( var, fun ):

	table = [  ]

	pos = 0

	for i in fun:
	
		table.append( getBin( i, var ) )

		table[ pos ][ var ] = 1

		pos += 1

	return table
