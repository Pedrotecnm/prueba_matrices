# Tarea 4
# Versión 2
# Despcripción: Aplicación de programación orientada a objetos para el manejo de operaciones básicas con matrices.
# Se crean dos clases: 
#   Clase Matriz para creación de las matrices y sus operaciones básicas
#   Clase Operaciones con matrices para las operaciones aritmeticas
#   Clase Interfaz para las actividades de entrada salida de datos
# Autor: Elizabeth Cuatecontzi Cuahutle, Tecnológico Nacional de México- Instituto Tecnológico de Apizaco
# Fecha: Septiembre 2024

#Definición de la clase Matriz
import os
import sys
def limpiar_consola():
    os.system('clear')

def termina_programa():
    sys.exit()

#Definición de la clase Matriz
class Matriz():
    def __init__(self,  filas=0, columnas=0):
        self.filas = filas
        self.columnas = columnas
        # crea una matriz de filas x columnas con elementos con valo de 0
        self.matriz=[[0 for _ in range(columnas)] for _ in range(filas)]

 # Permite acceder a los elementos de la matriz utilizando índices.
    def __getitem__(self, indices):  
        return self.matriz[indices]
    
    def __setitem__(self, index, value):
        self.matriz[index] = value

# Definición de la clase Interfaz  
class Interfaz(Matriz):
    def lee(matriz):
        c=0
        for fila in matriz:
            f=0
            for columna in fila:
                f+=1
            c+=1
        matriz=[]
        for i in range(c):
            fila = []
            for j in range(f):
                valor = float(input(f"Ingresa valor {i+1},{j+1}: "))
                fila.append(valor) # Agrega un valor a la matriz
            matriz.append(fila) # Agrega una fila a la matriz
        return matriz
    
    # muestra los elementos en la matriz
    def ver(matriz):
        for fila in matriz: # visualiza fila a fila la matriz
            print(fila)
        return
    
#Definición de la clase para la operación con matrices
class OperacionMatriz():
    # suma matrices
    def suma(matriz1, matriz2):
        # inicia en 0's la matriz resultante
        matrizr = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1[0]))]
        for i in range(len(matriz1[0])):
            for j in range(len(matriz1[0])):
                # suma cada elemento de la matriz
                matrizr[i][j]= matriz1[i][j]+matriz2[i][j] 
        return matrizr
       
    # resta matrices
    def resta(matriz1, matriz2):
        # inicia en 0 la matriz resultante
        matrizr = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1[0]))]
        for i in range(len(matriz1[0])):
            # resta cada elemento de la matriz
            for j in range(len(matriz1[0])):
                matrizr[i][j]= matriz1[i][j]-matriz2[i][j]
        return matrizr
    
    # multiplica  matrices
    def multiplica(matriz1, matriz2):
        # inicia en 0's la matriz resultante
        matrizr = [[0 for _ in range(len(matriz1[0]))] for _ in range(len(matriz1[0]))]
        filas = columnas = len(matriz1[0])
        for i in range(filas):
            for j in range(columnas):
                # multiplica cada elemento de la matriz
                for k in range(columnas):
                    matrizr[i][j]+=matriz1[i][k] * matriz2[k][j]
        return matrizr  
    
    # obtiene la transpuesta de la matriz
    def transpuesta(matriz):
        filas=columnas=len(matriz[0])
        matrizt =[[0 for _ in range(filas)] for _ in range(columnas)]
        for i in range(filas):
            for j in range(columnas):
                #cambia los elementos de una matriz
                matrizt[j][i
                           ] = matriz[i][j]
        return matrizt
                    
# Inicia programa principal
limpiar_consola()
print("PROGRAMA DE OPERACIONES CON MATRICES .... Inicia....")
print("!ADVERTENCIA! .... El programa permite la operación de matrices con igual número de filas y columnas; es decir cuadradas")

# Creación de la matriz 1
print()
print ("MATRIZ 1:")
n1=int(input("Ingresa el número de de filas"))
m1=int (input("Ingresa el número de columnas"))
M1=Matriz(n1,m1) 
M1=Interfaz.lee(M1)
Interfaz.ver(M1)

# Creación de la matriz 2
print()
print ("MATRIZ 2:")
n2=int(input("Ingresa el número de de filas"))
m2=int (input("Ingresa el número de columnas"))
M2=Matriz(n2,m2)
M2=Interfaz.lee(M2)
Interfaz.ver(M2)

#Operaciones con matrices
print()
print ("OPERACIONES CON MATRICES")
if not(n1==n2 and m1==m2): 
    print("!! No es posible realizar operaciones con matrices!!")
    print("!! Las matrices no son cuadradas!!")
    termina_programa()
# suma de matrices
print()
print ("Suma matrices")
Msuma=Matriz()
Msuma = OperacionMatriz.suma(M1,M2)
Interfaz.ver(Msuma)

# resta de matrices
print()
print ("Resta matrices")
Mresta=Matriz()
Mresta = OperacionMatriz.resta(M1,M2)
Interfaz.ver(Mresta)

# multiplicación de matrices
print()
print ("Multiplicación de matrices")
Mmultiplica=Matriz()
Mmultiplica = OperacionMatriz.multiplica(M1,M2)
Interfaz.ver(Mmultiplica)

# Transpuesta de las matrices
print()
print ("Transpuesta de la matriz 1")
MT1 = OperacionMatriz.transpuesta(M1)
Interfaz.ver(MT1)
print ("Transpuesta de la matriz 2")
MT2 = OperacionMatriz.transpuesta(M2)
Interfaz.ver(MT2)
print ("Transpuesta de la suma de matrices")
MTS = OperacionMatriz.transpuesta(Msuma)
Interfaz.ver(MTS)
print ("Transpuesta de la resta de matrices")
MTR = OperacionMatriz.transpuesta(Mresta)
Interfaz.ver(MTR)
print ("Transpuesta de multiplicación de matrices")
MTM = OperacionMatriz.transpuesta(Mmultiplica)
Interfaz.ver(MTM)

