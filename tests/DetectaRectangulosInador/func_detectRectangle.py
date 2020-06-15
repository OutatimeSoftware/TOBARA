from func_getBin import *
from func_getKmap import *

def reduceKmap( kmap ):

	forms = [ ]
	
	mask = kmap
	
	var = 4

	x = 0

	y = 0
	'''
	for line in mask:
		
		for cell in line:
		
			if( cell == 1 ):
				
				detectRectangle( kmap, mask, x, y, var, forms )

			x = ( x + 1 ) % var

		y += 1 
		'''
	detectRectangle( kmap, mask, x, 1, var, forms )


	if ( checkLineH( kmap, 1, 0, 0 ) ):

		print(" :D ")

def zeros( mask, form ):
	
	x, y = form[ 0 ][ 0 ], form[ 0 ][ 1 ]
	
	xf , yf = form[ 1 ][ 0 ] + 1, form[ 1 ][ 1 ] + 1

	for line in range( y, yf ):

		for cell in range( x, xf ):

			mask[ line ][ cell ] = 0

def	checkLineH( kmap, ref, ini, fin ):

	if ( ini < fin ):

		for position in range( ini, fin ):

			if( kmap[ ref ][ position ] != 1 ):

				return False
			
		return True

	else:

		for position in range( ini, fin - 1, -1 ):

			if( kmap[ ref ][ position ] != 1 ):

				return False
			
		return True
	
def	checkLineV( kmap, ref, ini, fin ):
	
	for position in range( ini, fin ):

		if( kmap[ position ][ ref ] != 1 ):

			return False
		
	return True

def detectRectangle( kmap, mask, x, y, var, forms ):

	origenX = x
	
	origenY = y

	while( kmap[ x ][ y ] == 1 ):

		if( checkLineH( kmap, x, origenX, x ) == False or checkLineV( kmap, y, origenY, y ) == False  ):

			break

		x += 1
			
		y += 1

	print( x, y )
	
	form = [ ( origenX, origenY ),
			 ( x, y ) ]

	zeros( mask, form )

	forms.append( form )

def main():

	# lista de mintérminos.
	fun = [ 0, 1, 2, 4, 5, 6, 7, 8, 9, 10 ]
	
	var = 4
	
	kmap = getKmap( var, fun )
	
	for line in kmap:
		
		print( line )
	
	reduceKmap( kmap )
	
if __name__ == "__main__":

    main()
