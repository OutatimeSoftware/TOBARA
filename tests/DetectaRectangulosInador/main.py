from func_getBin import *
from func_getKmap import *
	
def reduceKmap( kmap ):
	
	active = kmap
	
	x = 0
	
	y = 0
	
	for line in active:
		
		y += 1 
		
		x = 0
		
		for cell in line:
		
			x += 1
		
			if( cell == 1 ):
				
				print( x, y )
	
	
def main():

	# lista de mintérminos.
	fun = [ 0, 1, 2, 4, 5, 6, 8, 9, 10 ];
	var = 4
	Kmap = getKmap( var, fun )
		
	for line in Kmap:
		print( line )
		
	reduceKmap( Kmap )
	
if __name__ == "__main__":

    main()
