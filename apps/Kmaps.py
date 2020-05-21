import pygame

import numpy as np

def main():

	# inicializa pygame

	pygame.init()

	# titulo de la ventana

	pygame.display.set_caption('K-map')

	#Definicion de colores

	bg = (220, 220, 220)
	cyan = (0, 255, 255)

	#Declaracion de variables
	
	celdasX, celdasY = 4, 4
	
	kmap = np.zeros( ( celdasX, celdasY ) )
	
	#Creacion de pantalla

	width, height = 100 * celdasX, 100 * celdasY
	screen = pygame.display.set_mode((width, height))
	screen.fill(bg)
	
	# Actualizacion de pantalla
	
	pygame.display.flip()

	# bucle infinito
	while ( True ):
    	# obtiene un solo evento de la cola de eventos
		event = pygame.event.wait()
		
		#Creacion de la cadricula
		
		for y in range( 0, celdasY ):
			for x in range( 0, celdasX ):
				
				poly = [( ( x ) * 100, ( y ) * 100 ),
						( ( x + 1 ) * 100, ( y ) * 100 ),
						( ( x + 1 ) * 100, ( y + 1 ) * 100 ),
						( ( x ) * 100, ( y + 1 ) * 100 ) ]
				
				pygame.draw.polygon( screen, ( 160, 160, 160 ), poly, 1 )

		pygame.display.flip()

		# si se presiona el botón 'cerrar' de la ventana
		if event.type == pygame.QUIT:
			# detiene la aplicación
			break

	# finaliza Pygame
	pygame.quit()

if __name__ == '__main__':
    main()
