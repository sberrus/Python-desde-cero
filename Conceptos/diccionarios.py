# DICCIONARIOS:
# *Los diccionarios son estructuras de datos similares a los arrays y las tuplas, pero que estas nos permiten en vez de usar indices para acceder a sus posiciones, utiliza Strings para acceder a un valor dentor del diccionario.
# *Básicamente es un objeto pero de un solo nivel el cual se accede mediante su namespace dentro de corchetes.

# *Inicialización de un diccionario.
diccionario = {
    "nombre": "Samuel",
    "edad": 23,  # *Acepta strings e int
    "estado": "confuso",
}

print(diccionario)
print(diccionario["nombre"])

# *Este método sirve para complicarse la vida.
print(diccionario.get("estado"))
diccionario["nombre"] = "que raro es python"
print("Diccionario con valor cambiado:", diccionario)

# *Los diccionarios son Mutables. Estos nos permiten ingresar un par clave-valor directamente.
diccionario["nuevo estado"] = "se puede?"
print("Añadiendo nuevo valor al diccionario:", diccionario)

# *Con el método len() obtenemos el alcance del diccionario.
print(len(diccionario))
