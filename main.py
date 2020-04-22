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
	
		if ( ord(fun[i]) > mayor and ord(fun[i]) <= 122 ):
	
			mayor = ord(fun[i])
	
		elif ( ord(fun[i]) < menor and ord(fun[i]) >= 97 ):
	
			menor = ord(fun[i])

	return mayor - menor + 1
	
	

def getTer( fun ):

    terminos = 1

    for variable in fun:
        if (variable == '+'):
            terminos += 1
            
    return terminos
			
def generateTable( boolfun, var ):
	
	table = []
	
	tam = y = 2 ** var 
	
	for i in range( y ):
	
		table.append([])
		
		for j in range( var + 1 ):
			
			table[ i ].append( 0 )		
	
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
