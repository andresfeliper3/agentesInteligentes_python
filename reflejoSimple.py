import numpy as np 
from Rata import Rata

#CONSTANTES
VACIO = 0
MURO = 1
QUESO = 2
RATA = 3

"""
En un ambiente:
0: vacío
1: muro
2: queso
3: rata
Lectura del archivo de ambiente
"""
ambiente = np.genfromtxt('archivos/ambiente.txt', delimiter=' ')
ambiente = ambiente.astype(int)

# Encontrar la posicion de la rata en el ambiente inicial
def hallarPosicionRata():
  for i in range(len(ambiente)):
    for j in range(len(ambiente[0])):
      if(ambiente[i][j] == RATA):
        return i,j
  return None      


"""
En la matriz de decisión:
0: libre / no huele a queso
1: no libre / huele a queso
En las acciones:
0: izquierda
1: arriba
2: derecha
3: abajo
-1: movimiento no válido

Leer tabla de decisión del archivo en matriz Filas
"""
filas = np.genfromtxt('archivos/tablaDecision.txt', delimiter=' ')
filas = filas.astype(int)

"""
 Función para crear matriz de decisión donde los índices indican lo que se ve
"""
def crearMatrizDecision():
  matrizDecision = np.empty((2, 2, 2, 2))
  for fila in filas:
    matrizDecision[fila[0]][fila[1]][fila[2]][fila[3]] = fila[4]
  return matrizDecision.astype(int)

matrizDecision = crearMatrizDecision()

#Creacion de rata
filaRata, columnaRata = hallarPosicionRata()
rata = Rata(filaRata, columnaRata)

# Ejecución automática según la tabla de decisión 
# Se detiene si encuentra el queso o con un número máximo de movimientos
counter = 0
while not rata.tuvoExito and counter<=10: 
  rata.definirMovimiento(ambiente, matrizDecision)
  rata.moverse(ambiente)
  print("Estado del ambiente", counter)
  print(ambiente)
  counter += 1

if rata.tuvoExito:
  print("La rata encontró el queso")
