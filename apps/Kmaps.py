import pygame
import numpy as np
import time

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
	cellSize = 50
	
	kmap = np.zeros( ( varX, varY ) )
	
	#Creación de pantalla

	width, height = varX * cellSize, varY * cellSize 
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
			mouseClick = pygame.mouse.get_pressed()
			
			if( sum(mouseClick) > 0 ):
			
				posX, posY = pygame.mouse.get_pos()
				
				celX, CelY = int( posX / cellSize ), int( posY / cellSize )
				
				kmap[ celX, CelY ] = not mouseClick[ 2 ]
				
		#Creacion de la cadricula
		
		for y in range( 0, varY ):
		
			for x in range( 0, varX ):
				
				poly = [( ( x ) * cellSize, ( y ) * cellSize ),
						( ( x + 1 ) * cellSize, ( y ) * cellSize ),
						( ( x + 1 ) * cellSize, ( y + 1 ) * cellSize ),
						( ( x ) * cellSize, ( y + 1 ) * cellSize ) ]
				
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
