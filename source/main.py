from func_getBin import *
from func_getKmap import *
from func_getTable import *
from func_getMinTable import *
	
def main():

	# lista de mintérminos.
	fun = [ 0, 3, 12, 15 ];
	var = 4
	Kmap = getKmap( var, fun )
	table = getTable( var, fun )
	minTable = getMinTable( var, fun )
	
	print(  )
	
	print( "Los mintérminos de la función ingresada son: {}".format( fun ) )
	
	print(  )
	
	print( "La tabla de verdad de la función es: " )
	
	for i in table:
		
		print( "", end = " " )
		
		print( i )

	print(  )

	print( "La tabla de mintérminos de la función es:" )
	
	for i in minTable:
		
		print( "", end = " " )
		
		print( i )
	
	print(  )
	
	print( "El Kmap de la función es: " )

	for i in Kmap:
		
		print( "", end = " " )
		
		print( i )
	
if __name__ == "__main__":

    main()
