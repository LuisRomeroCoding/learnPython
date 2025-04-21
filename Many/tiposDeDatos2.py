# Tipos de datos 2

# COLECCIONES
# Son tipos de datos que permiten almacenar multiples elementos en una sola variable y dichos
# datos pueden ser de cualquier tipo como string, int, bool e incluso otras colecciones.

# LIST - Listas
# Son ordenadas, mutables y permite duplicar valores
miLista = [1, 2, 3, "Lista", True]
# print(miLista)
# miLista[1] = 6

# TUPLE - Tuplas
# Son ordenadas, permiten valores duplicados, son INMUTABLE
miTupla = (1, 2, 3, "Tupla", True)
# print(miTupla)
# miTupla[1] = 45

# SET - Conjuntos
# No son ordenados, No permite elementos duplicados y Son mutables
miConjunto = {1, 2, 3, 4, 5, 1, 2}
# print(miConjunto)
# miConjunto.add(23)
# miConjunto.remove(3)

# DICT - Diccionario
# Son colecciones en las que cada elemento viene en pareja clave -> valor
# Son mutable y agilizan la busqueda de elementos por clave
miDiccionario = {
    "nombre": "Patroclo",
    "edad": 32,
    "estatura": "1.7m"
}
# miDiccionario["edad"] = "33"
# miDiccionario["peso"] = 81
# miDiccionario.update({ "peso": 80, "auto": True })

print(miLista)
print("")
print(miTupla)
print("")
print(miConjunto)
print("")
print(miDiccionario)