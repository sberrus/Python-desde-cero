# PROFUNDIZACIÓN DE LOS DICCIONARIOS.
# !Para profundizar ver primero diccionarios.py

# Diccionario Base
usuario = {
    "nombre": "Samuel",
    "apellido": "Berrus",
    "edad": 23,
    "toDelete": "true"
}

# *Agregar nueva clave-valor.
print("\n")
usuario["pais nacimiento"] = "Venezuela"
print("Agregado nueva clave-valor:", usuario, "\n")

# *Eliminar valor del diccionario método 1.
usuario.pop("toDelete")
print("Eliminada clave toDelete:", usuario, "\n")

# *Eliminar valor del diccionario método 2.
del usuario["apellido"]
print("Eliminada clave toDelete:", usuario, "\n")

# *Eliminar último valor del diccionario.
usuario.popitem()
print("Eliminado último valor del diccionario:", usuario, "\n")

# *Copiando diccionario Método 1.
usuario_copiado = usuario.copy()
print("diccionario copiado:", usuario_copiado, "\n")

# *Copiando diccionario Método 2.
usuario_copiado2 = dict(usuario)
print("diccionario copiado método 2:", usuario_copiado2, "\n")

# *Limpiar diccionario.
usuario.clear()
print("diccionario 'usuario' vaciado:", usuario, "\n")
