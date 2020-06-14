# Notas temporales
## Destruir después de implementarlo en la bitácora.

Aprovecho para definir de manera más clara el proceso del algoritmo ( al menos la idea que estoy pensando ahora ).

Tenemos dos matrices, el original que nunca se modificará y un detector de puntos.
El original nos servirá para hacer más copias para detectar los cuadrados sin inteferir en colisiones.

El detector de puntos ( active ) Servirá para marcar cuales son las formas que se han encontrado hasta ahora, la idea es capturar a los terminos incompletos mediante la busqueda de rectangulos que cumplan las condiciones:

1. El rectangulo debe ser potencia de 2.
2. El rectangulo más grande será el termino principal.

En si, al desmarcar los activos en el detector de puntos, nos quedarán los posibles rectangulos que no se han formado en las anteriores busquedas, sea del tamaño que sea.

Ahora, para la captura de los rectangulos se guardaran mediante 4 coordenadas que indican el tamaño del rectangulo.

Todas estas serán guardadaras en una lista llamada MinTerms [] que serán las expresiones minimas de la función.

Una vez sacados todos los minTerms, podemos pasar a la interpretación de los rectangulos, pero eso sera apenas se termine y compruebe el funcionamiento de la función reduceKmap()
Con suerte mañana lo termino
