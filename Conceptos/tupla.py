# * Las tuplas son un tipo de array que ofrece python que nos permite crear un array pero que este sea inmutable. Este se inicializa usando los paréntesis () en ves de los corchetes [].
# * Las tuplas son mucho más básicas que los arrays

tupla = ("Hola", "Mundo")
print(tupla)

# * METODOS DISPONIBLES PARA LAS TUPLAS
print("Método .count('Hola'):", tupla.count("Hola"))
print("Indice de 'Hola':", tupla.index("Hola"))
print("Acceder a contenido almacenado en el indice 1:", tupla[1])
print("Parsear una tupla a array:")
listaDeTupla = list(tupla)  # *Este método vuelve una tupla un array.
print("Imprimir tupla parseada a array:", listaDeTupla)
tuplaSinParentesis = "de", "esta", "forma", "tambien", "podemos", "crear", "tuplas"
print(tuplaSinParentesis)

