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
	
def detectRectangle( kmap, x, y ):
	
	
	

def main():

	# lista de mintérminos.
	fun = [ 0, 4 ]
	var = 4
	
	kmap = getKmap( var, fun )
	
	reduceKmap( kmap )
	
if __name__ == "__main__":

    main()
