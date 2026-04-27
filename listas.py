#En este script vamos a trabajar ejemplos de formulación de listas.
#Creación de una lista nueva:
nombres = list()
n = int(input("Ingrese la cantidad de nombres que desea añadir: "))

for i in range(n):
    nombre = input("Ingrese otro nombre: ")
    nombres.append(nombre)
    
print(nombres)