def generateTable( boolfun, var ):
	
	table = []
	
	tam = y = 2 ** var 
	
	for i in range( y ):
	
		table.append([])
		
		for j in range( var + 1 ):
			
			table[ i ].append( 0 )		
	
	return table
