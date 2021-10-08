# PALABRA RESERVADA del

# *La palabra reservada "del" sirve para eliminar valores dentro de arreglos o diccionarios.

# * Usando del en diccionarios
usuario = {"hola": "mundo", "adios": "mundo"}
print("\n")
print("Diccionario:", usuario)
del usuario["hola"]
print("Usando palabra reservada 'del':", usuario, "\n")

# * Usando del en array
nombres = ["pedro", "jose", "maria"]
print("Array:", nombres)
del nombres[2]
print("Usando 'del'", nombres, "\n")
