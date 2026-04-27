#En este script vamos a gestionar la reserva de asientos en un vuelo de dimensiones 7x20:
#Lista que contiene las filas:

filas = list() #Por defecto está vacía:
for i in range(20):
    columna = list()
    for p in range(7):
        columna.append("*")
    filas.append(columna)

reservas = int(input("Ingrese la cantidad de reservas: "))

for i in range(reservas):
    pos_x = int(input("Ingrese la columna de su asiento"))
    pos_y = int(input("Ingrese la fila de su asiento"))
    filas[pos_x-1][pos_y-1] = "X"

#Imprimir la cuadrícula del avión:
for k in range(20):
    for m in range(7):
        print(filas[k][m], end='')
    print("")