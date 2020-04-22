def main():
	boolFun = getFun()
	printTable ( generateTable( boolFun, getVar( boolFun ) ), getVar( boolFun ) )	

def getFun():
	boolFun = input()
	return boolFun.lower()
	
def getVar( fun ):
	tam = len( fun )
	menor = mayor = ord( fun[ 0 ] )
	for i in range( tam ):
		if ( ord(fun[i]) > mayor ):
			mayor = ord(fun[i])
		elif ( ord(fun[i]) < menor ):
			menor = ord(fun[i])
	return mayor - menor + 1
	
def getMen( fun ):
	tam = len( fun )
	menor = ord( fun[ 0 ] )
	for i in range( tam ):
		if ( ord(fun[i]) < menor ):
			menor = ord(fun[i])
	return menor + 1
	
def getTer( fun ):
	tam = len( fun )
	terminos = 1
	for i in range( tam ):
		if ( fun[i] == "+" ):
			terminos += 1
			
def generateTable( boolfun, var ):
	print(var)
	table = []
	for i in range( 2 ** var  ):
		table.append( [0] * ( var + 1 ) )
	return table
	
def printTable( table, var ):
	for i in range( 2 ** var ):
		for j in range( var + 1 ):
			if( j >= var ):
				print("|", end = " ")
			print(table[i][j], end = " ")
		print()
	
if __name__ == "__main__":
    main()
