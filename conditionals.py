#CONDICIONALES(if-else):

#Los condicionales son estructuras que permiten evalúar el cumplimiento o no condiciones lógicas(sólo con dos valores posibles) para la ejecución de acciones concretas.
#                        ____________________
#----Dato de entrada--->| Condición a evaluar|---Acción de salida-->
#                       |    Cumple o no     |
#                        ____________________
#En Python estos condicionales siguen una estructura muy sencilla definida por tres estructuras if-elif-else.
edad = int(input("Ingrese su edad para clasificarla"))

if edad>=0 and edad<=17:
    print("Eres muy joven")
elif edad>=18 and edad<=28:
    print("Eres un adulto joven")
elif edad>=29 and edad<45:
    print("Adulto maduro")
elif edad>=46:
    print("Adulto mayor")
else:
    print("Edad no válida")