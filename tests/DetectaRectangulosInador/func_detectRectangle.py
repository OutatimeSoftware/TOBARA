from func_getBin import *
from func_getKmap import *

def reduceKmap( kmap ):
	
	mask = kmap
	
	x = 0
	
	y = 0
	
	for line in mask:
		
		y += 1 
		
		for cell in line:
		
			x = ( x + 1 ) % 4
		
			if( cell == 1 ):
				
				detectRectangle( kmap, mask, x, y )
			
def	checkLineH( kmap, ref, start, end ):
	
	pass
	

def detectRectangle( kmap, mask, x, y ):
	
	rect = [ ( x, y ), ( x, y ) ]
	
	while( kmap[ x + 1  ][ y + 1 ] ):
		
		 x += 1
		 y += 1
		
		print( "Active" )
	
	#Extra para ver cuantas veces entra la función
	print( x, y )
	
	

def main():

	# lista de mintérminos.
	fun = [ 0, 4 ]
	
	var = 4
	
	kmap = getKmap( var, fun )
	
	reduceKmap( kmap )
	
if __name__ == "__main__":

    main()
