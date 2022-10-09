
# Agentes Inteligentes en Python
Código de una rata que cruza un laberitno usando agentes inteligentes.

## Agente de reflejo simple
En la carpeta de archivos se pueden editar los archivos de *ambiente.txt* y *tablaDecision.txt*.

### Archivo de ambiente

El archivo de ambiente permite editar el laberinto inicial al cual se va a enfrentar el agente.
Se debe interpretar como una cuadrícula donde cada número representa el estado de una casilla.

| Número | Significado |
| ----------- | ----------- |
| 0 | Vacío (accesible) |
| 1 | Muro (inaccesible) |
| 2 | Queso (objetivo) |
| 3 | Rata (agente) |

Así, un ejemplo de ambiente sería:

![Ejemplo de laberinto](/assets/ejemplo_laberinto.png "Ejemplo")

Que en el archivo de texto se expresaría de la siguiente forma.
| - | - | - | - |
| ----------- | ----------- | ----------- | ----------- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 2 |
| 3 | 1 | 0 | 0 |
| 0 | 0 | 0 | 1 |

Las separaciones entre filas se hacen con **un salto de línea** y las separaciones entre columnas se hace con **un espacio en blanco**.

---

### Archivo de tabla de decisión

El archivo de tabla de decisión tiene las asociaciones entre las percepciones con sus respectivas acciones.
Las columnas marcan los diferentes sensores excepto la última que indica la acción asociada.
- Primera columna: sensor izquierdo.
- Segunda columna: sensor arriba.
- Tercera columna: sensor derecho.
- Cuarta columna: sensor abajo.
- Quinta columna: acción.

Los sensores pueden recibir dos posibles valores: 0 (cero) y 1 (uno). 
| Valor en el sensor | Significado |
| ----------- | ----------- | 
| 0 | libre |
| 1 | no libre | 

Las acciones pueden recibir los posibles valores:
| Valor en la acción | Significado |
| ----------- | ----------- | 
| -1 | no válido |
| 0 | ir izquierda | 
| 1 | ir arriba | 
| 2 | ir derecha |
| 3 | ir abajo |

### Ejecutar código
Para ejecutar el código, se debe correr el comando `python3 reflejoSimple.py` o `py reflejoSimple.py` desde la carpeta donde están contenidos los archivos. 


