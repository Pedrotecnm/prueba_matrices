#Tarea 4
# Versión 1
# Despcripción: Aplicación de programación orientada a objetos para el manejo de operaciones básicas con matrices.
# Se maneja una clase: 
# Clase Matriz para creación de las matrices, sus operaciones básicas y operaciones aritmeticas,
# Los resultados quedan en la primera matriz
# Autor: Elizabeth Cuatecontzi Cuahutle, Tecnológico Nacional de México- Instituto Tecnologico de Apizaco
# Fecha: Septiembre 2024

#Definición de la clase Matriz
class Matriz():
    def __init__(self, nombre, filas=0, columnas=0):
        self.nombre=nombre
        self.filas = filas
        self.columnas = columnas
        self.matriz=[]

    def __getitem__(self, indices):
# Permite acceder a los elementos de la matriz utilizando índices.
        return self.matriz[indices]

    def __setitem__(self, index, value):
        self.matriz[index] = value

# Leer y almacenar los elementos en la matriz
    def leer(self):
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                valor = float(input(f"Ingresa valor {i+1}, {j+1}: "))
                fila.append(valor)
            self.matriz.append(fila)

# visualizar los elementos en la matriz
    def ver(self):
        print (self.nombre)
        for fila in self.matriz:
            print(fila)
    
# suma matrices, el resultado queda en la primera matriz
    def suma(self, matriz2):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j]= self.matriz[i][j]+matriz2[i][j]     
    
# resta matrices, el resultado queda en la primera matriz
    def resta(self, matriz2):
        for i in range(self.filas):
            for j in range(self.columnas):
                self.matriz[i][j]-=matriz2[i][j]     
    
# resta matrices, el resultado queda en la primera matriz
    def multiplica(self, matriz2):
        matrizp = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]
        for i in range(self.filas):
            for j in range(self.columnas):
                for k in range(self.columnas):
                    matrizp[i][j]+=self.matriz[i][k] * matriz2[k][j]
        self.matriz=matrizp         

# Transpuesta de  matriz
    def transpuesta(self):
        mtranspuesta = [[0 for _ in range(self.filas)] for _ in range(self.columnas)]
        for i in range(self.filas):
            for j in range(self.columnas):
                mtranspuesta[j][i] = self.matriz[i][j]
        self.matriz=mtranspuesta

print("OPERACIONES CON MATRICES.... Inicia....")
print("El programa permite la operación con igual número de filas y columnas; es decir cuadradas")
n=m = int(input("Ingresa el número de de filas y columnas"))

# Creación de la matriz 1
print()
print("MATRIZ 1")
M1 = Matriz("Matriz 1",n,m)
M1.leer()
M1.ver()

# Creación de la matriz 2
print()
print ("MATRIZ 2")
M2 = Matriz("Matriz 2", n,m)
M2.leer()
M2.ver()

# Suma matriz 1 con matriz 2, el resultado queda en matriz 1
print()
print ("SUMA")
M1.suma(M2)
M1.ver()

# Resta matriz 1 con matriz 2, el resultado queda en matriz 1
print()
print("RESTA")
M1.resta(M2)
M1.ver()

# Multiplica matriz 1 con matriz 2, el resultado queda en matriz 1
print()
print("MULTIPLICA")
M1.multiplica(M2)
M1.ver()

# Obtiene la transpuesta de matriz 1
print()
print ("Transpuesta")
M1.transpuesta()
M1.ver()        
