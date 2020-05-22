import pygame
import numpy as np
import time

def info( screen, noTer ):
   
	font = pygame.font.Font( None, 30 )
   
	minTerminos = font.render( "Mintérminos" + str( noTer ), 1, ( 160, 160, 160 ) )
   
	screen.blit( minTerminos, ( 2, 3) )


def main():

	# inicializa pygame

	pygame.init()

	# título de la ventana

	pygame.display.set_caption('The Game Of Life')

	#Definición de colores

	bgFalse = ( 220, 220, 220 )
	border = ( 160, 160, 160 )
	bgTrue = ( 220, 237, 160 )

	#Declaración de variables
	
	varX, varY = 4, 4
	cellSize = 75
	noTer = 0
	
	kmap = np.zeros( ( varX, varY ) )
	
	#Creación de pantalla

	width, height = varX * cellSize, ( varY * cellSize ) + 50
	screen = pygame.display.set_mode( ( width, height ) )
	screen.fill( bgFalse )
	
	# Actualizacion de pantalla
	
	pygame.display.flip()

	# bucle infinito
	while ( True ):
    	# Obtiene un solo evento de la cola de eventos
		event = pygame.event.wait()
		
		ev = pygame.event.get()
		
		for event in ev:
			
			#Detectar interacci[on con el mouse
			click = pygame.mouse.get_pressed()
			
			if( sum( click ) > 0 ):
			
				posX, posY = pygame.mouse.get_pos()
				
				celX, celY = int( posX / cellSize ), int( ( posY - 50 ) / cellSize )
				
				if( not click[ 2 ] ):
				
					if( not kmap[ celX, celY ] ):
					
						noTer += 1
						
						kmap[ celX, celY ] = True
					
				elif( kmap[ celX, celY ] ):
					
						noTer -= 1
						
						kmap[ celX, celY ] = False
			
		#Creacion de la cadricula
		
		for y in range( 0, varY ):
		
			for x in range( 0, varX ):
				
				poly = [( ( x ) * cellSize, 	( ( y ) 	  * cellSize ) + 50 ),
						( ( x + 1 ) * cellSize, ( ( y ) 	  * cellSize ) + 50 ),
						( ( x + 1 ) * cellSize, ( ( y + 1 )	  * cellSize ) + 50 ),
						( ( x ) * cellSize, 	( ( y + 1 )   * cellSize ) + 50 ) ]
				
				if( kmap[ x, y ] == 0 ):
					pygame.draw.polygon( screen, bgFalse, poly, 0 )
					pygame.draw.polygon( screen, border, poly, 1 )
				else:
					pygame.draw.polygon( screen, bgTrue, poly, 0 )
					pygame.draw.polygon( screen, border, poly, 1 )

		pygame.display.flip()

		# si se presiona el botón 'cerrar' de la ventana
		if event.type == pygame.QUIT:
			# detiene la aplicación
			break

	# finaliza Pygame
	pygame.quit()

if __name__ == '__main__':
    main()
