from func_getBin import *
from func_getKmap import *

def reduceKmap( kmap ):

	forms = [ ]
	
	mask = kmap
	
	var = 4

	x = 0
	
	y = 0

	for line in mask:
		
		for cell in line:
		
			if( cell == 1 ):
				
				detectRectangle( kmap, mask, x, y, var, forms )

			x = ( x + 1 ) % 4

		y += 1 

	for item in forms:

		print( item )

def zeros( mask, form ):
	
	x, y = form[ 0 ][ 0 ], form[ 0 ][ 1 ]
	
	xf , yf = form[ 1 ][ 0 ] + 1, form[ 1 ][ 1 ] + 1

	for line in range( y, yf ):

		for cell in range( x, xf ):

			mask[ line ][ cell ] = 0

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

def detectRectangle( kmap, mask, x, y, var, forms ):

	origenX = x
	
	origenY = y

	while( kmap[ x ][ y ] == 1 ):
			
		if ( checkLineH( kmap, x ) == False or checkLineV( kmap, y ) == False ):
				
			break
			
		x += 1
			
		y += 1
	
	x -= 1

	y -= 1

	print( x, y )

	while( kmap[ x ][ y ] == 1 ):

		if( checkLineV( kmap, y - 1 ) == False ):

			break

		x += 1
	
	form = [ ( origenX, origenY ),
			 ( x, y ) ]

	zeros( mask, form )

	for line in mask:
		
		print( line )

	forms.append( form )

def main():

	# lista de mintérminos.
	fun = [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 13, 14 ]
	
	var = 4
	
	kmap = getKmap( var, fun )
	
	for line in kmap:
		
		print( line )
	
	reduceKmap( kmap )
	
if __name__ == "__main__":

    main()
