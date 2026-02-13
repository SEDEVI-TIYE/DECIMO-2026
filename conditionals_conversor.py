#PROGRAMA: MULTICONVERSOR DE MEDIDAS(REPASO CONDICIONALES)
print("ELija entre las siguientes opciones: ")
print("1. °C a F, 2. kg a lb, 3. m a ft , 4.lt a gal 5. km a yd: ")

option = int(input()) 

if option==1:
    print("Inserte los grados °C a convertir: ")
    celsius = float(input())
    farenheit = celsius*1.8 + 32
    print("La temperatura en °F es: ",farenheit)
elif option==2:
    print("Inserte los de kg a convertir: ")
    kg = float(input())
    lb = kg*2.202
    print("La cantidad de libras: ", lb)
    
