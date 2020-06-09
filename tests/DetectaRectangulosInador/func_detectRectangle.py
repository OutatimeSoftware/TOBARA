from func_getBin import *
from func_getKmap import *

def reduceKmap( kmap ):
	
	mask = kmap
	
	x = 0
	
	y = 0
	"""
	for line in mask:
		
		y += 1 
		
		for cell in line:
		
			x = ( x + 1 ) % 4
		
			if( cell == 1 ):
				
				detectRectangle( kmap, mask, x, y, 1 )
	"""
	detectRectangle( kmap, mask, x, y, 1 )
			
def	checkLineH( kmap, ref ):
	
	x = ref
	
	while( x > 0 ):
	
		if( kmap[ ref ][ x ] != 1 ):

			return False			
			
		x -= 1
		
	return True
	
def	checkLineV( kmap, ref ):
	
	x = ref
	
	while( x > 0 ):
	
		if( kmap[ x ][ ref ] != 1 ):

			return False			
			
		x -= 1
		
	return True

def detectRectangle( kmap, mask, x, y, var ):
	
	origenX = x
	
	origenY = y

	if( x == y ):
		
		while( kmap[ x ][ y ] == 1 ):
			
			if ( checkLineH( kmap, x ) == False or checkLineV( kmap, y ) == False ):
				
				break
			
			x += 1
			
			y += 1
			
	form = [ ( origenX, origenY ), 
			 ( ( x - 1 ), ( y - 1 ) ) ]

	print( form )

def main():

	# lista de mintérminos.
	fun = [ 0, 1, 2, 4, 5, 6, 8, 9, 10, 12, 13, 14 ]
	
	var = 4
	
	kmap = getKmap( var, fun )
	
	for line in kmap:
		
		print( line )
	
	reduceKmap( kmap )
	
if __name__ == "__main__":

    main()
