# Actualizado 21 de Mayo 2020
# Función funcional
def getKmap( var, fun ):
	
	Kmap = [  ]
	
	for i in range( var ):
		
		Kmap.append( [ ] )
		
		for j in range( var ):
		
			Kmap[ i ].append( 0 )

	for minTer in fun:
		
		x = ( minTer ) // var
		
		y = ( minTer ) % var
		
		Kmap[ y ][ x ] = 1
		
	return Kmap
