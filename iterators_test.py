#TABLAS DE MULTIPLICAR 
#El objetivo de este programa es generar un algortimo que mediante el uso de iteradores permita desplegar una tabla de multuplicar elegida por el usuario la cantidad de términos también requridos por el usuario.


#Creación de variables:
#Ocuparemos dos variables para la recepción de los datos del usuario, la tabla y los términos:

tabla = int(input("Ingrese la tabla de multiplicar que desea desplegar: "))

terms = int(input("Ingrese la cantidad de términos que desea desplegar: "))

for i in range(terms):
    print(tabla," * ",i+1," = ",tabla*(i+1))
    

