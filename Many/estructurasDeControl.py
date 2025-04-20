# Las estructuras de control son herramientas que nos permiten controlas el flujo de
# ejecucion de un programa. Nos ayudan a decidir que instrucciones se ejecutan, cuando y cuantas
# veces.

# Condicionales
# Sirven para ejecutar codigo solo cuando se cumple una condicion.

# IF
edad = 13

if edad >= 18: 
    # if: el codigo dentro de if se ejecutara si se cumple la condicion
    print("Eres mayor de edad.")
elif edad > 12:
    # elif: en caso de que if no se cumpla y existe un elif con una nueva condicion se ejecutara en caso de que se cumpla. 
    # Si no se cumple continuara al siguiente elif, en caso de existir, si no continuara con el siguiente else.
    print("Eres un adolescente.")
else:
    # else: es el ultimo paso. En caso de no cumplirse las condiciones anteriores se ejecutara el codigo dentro del else.
    print("Eres un niño.")

print("")

# Bucles: sirven para iterar sobre una secuencia, como listaso o cadenas, 
# o repetir una accion mientras que una condicion se cumpla.

# FOR
lista = [1, 2, 3, "Hola", True]
for i in lista:
    print("Elemento: ", i)

print("")

# WHILE
contador = 0
while contador < 5:
    print("Contador: ", contador)
    contador += 1