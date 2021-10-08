# Métodos para arrays
array_base = []
print("Array base para ejemplos:", array_base)

# Método para asignar hacer push a array
# * Igual a método push de JS
array_base.append(1)
array_base.append(2)
array_base.append(5)
array_base.append(5)
print("Array base con nuevos valores:", array_base)

# Método para copiar los valores de un array
# * Parecido a "Spread Operator" en JS
array_copiado = array_base.copy()
print("Nuevo array con valores copiados de array báse:", array_copiado)

# Método para contar valores repetidos dentro de un array
coincidencias = array_base.count(5)
print("Número de veces que se repite el valor 5:", coincidencias)

# Método para saber la longitud de elementos de un array:
longitud = len(array_base)
print("La longitud total del array_base actualmente es de:", longitud)

# Acceder a elementos de un array
primer_elemento = array_base[0]
segundo_elemento = array_base[1]
print("El primer elemento del array base:",
      array_base, "es:", primer_elemento)
print("El segundo elemento del array base:",
      array_base, "es:", segundo_elemento)


# Eliminar último elemento de un array.
asistentes = ["Samuel", "Hellen", "Eilan", "Ori"]
print(asistentes.pop())  # Devuelve el último elemento del array.
print(asistentes)

# Eliminar un elemento en especifico de un array.
ciudades = ["Madrid", "Barcelona", "Cataluña", "Caracas"]
ciudades.remove("Cataluña")
print(ciudades)

# Revertir orden de un array.
paises = ["España", "Francia", "Paises Bajos", "Alemania"]
print("Orden Inicial del array:", paises)
paises.reverse()
print("Array Revertido", paises)

# Ordenar elementos de un array.
# * Los arrays deben tener un mismo tipo de datos, de lo contrario la función no funcionará :p
paises.sort()
print("Array de paises ordenado:", paises)
