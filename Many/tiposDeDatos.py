# 1. Crearemos un nuevo archivo llamado tiposDeDatos.py donde veremos los tipos de
#    datos basicos de python y como definirlos.

#Numericos
miEdad = 31 # int -> sin decimales
miEstatura = 1.70 # float -> con decimales
miPeso = 83.9

#Texto -> string o str
#Puede ser entre comillas simples('') o dobles("") 
miNombre = "Luis Manuel"
misApellidos = 'Romero Garcia'

#Booleanos -> sus valores solo pueden ser true(verdadero) o false(falso)
soyHombre = True
soyMenorDeEdad = False

#Conversion entre tipos de datos
int("14")
float("3.1416")
str(100)

print("Nombre: " + miNombre, "Edad: " + str(miEdad) + " años", "Estatura: " + str(miEstatura) + "cm")
print("")
print("Nombre: " + miNombre)
print("Apellidos: " + misApellidos)
print("Edad: " + str(miEdad) + " años")
print("Estatura: " + str(miEstatura) + "cm")
print("Peso: " + str(miPeso) + "kgs")