#Introducción a Python:
#Python es un lenguaje de programación interpretado, eso quiere decir que la ejecución de un programa se hará línea por línea y de forma individual por lo que un error no necesariamente detendrá la ejecución del proceso a diferencia de otros lenguajes como C++ o Java.

#Lenguaje compilado:                |  #Lenguaje interpretado:
#"Ve y abre la ventana"             |  "Ponte de píe, da dos pasos
#La instrucción se toma en su       |   hacia el costado derecho del
#conjunto y sí algún paso no        |   aula,estira la mano, gira el
#es claro detiene toda la ejecución.|   perno y empuja suavemente la 
#Suele ser más rápido de ejecutar.  |   ventana"
#                                   |   Ejecución línea por línea
#                                   |   En general más lento


#Una introducción sencilla:
#Cómo comunicarnos con el lenguaje de programación:
#Mostrar información por pantalla print()
print("Hola mundo!!")
variable = 216
texto = "Colombia"
print("Hola yo vivo en ",texto, " un país hermoso, que tienen unos ",variable," años de fundación, ya que el grito de independencia se dió en el año ",2026-variable)

#La función print nos permite diferentes tipos de impresión: textos literales(rodeados por comillas), variables(de cualquier tipo), operaciones matemáticas.

#En complemento a la función print tenemos la función input que nos permite ingresar información que va a ser guardada en espacios de memoria llamados variables:

dato = input("Ingresa tu nombre: ")
print("El nombre ingresado es: ",dato)

#La función input() recibe datos de tipo texto por defecto, sin embargo si queremos recibir datos de otro tipo podemos realizar un proceso llamado conversión de tipo de dato o en inglés(casting).

edad = int(input("Ingresa tu edad: "))
print("La edad ingresada es: ",edad)
print("Tu año aproximado de nacimiento es: ",2026-edad)

#Variables y tipos de datos:
#Cómo se mencionó previamente, la información puede ser guardada por medio de espacios de memoria conocidos como variables, los cuales pueden contener diferentes tipos de información o datos, a saber:
#(int) Números enteros: Valores sin parte decimal
#(float) Números decimales: Valores con parte decimal
#(bool) Valores lógicos: Verdadero o Falso(True o False)
#(string) Textos o caracteres: En general contenidos entre comillas

logic = True 
number = 1234
decimal = 3.1416
string = "Johanessburgo"

print(type(logic))
print(type(number))
print(type(decimal))
print(type(string))


#Operadores: Los operadores son los símbolos que emplearemos para las diferentes operaciones matemáticas y lógicas dentro de nuestro código:
#                            MATEMÁTICOS:
#Suma: +
#Resta: -
#Multiplicación: *
#División con decimales: /
#División sin decimales: //
#Operación módulo: % Devuelve el residuo de una división
#Potenciación: **
#                            LÓGICOS
#Mayor qué: >
#Menor qué: <
#Mayor o igual a: >=
#Menor o igual a:<=


