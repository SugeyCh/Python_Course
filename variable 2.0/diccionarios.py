# Creando un diccionario con la función dict()
dicc = dict(nombre="Pepe", apellido="Sanchez")
print(dicc)

# Otra forma de crear diccionarios pero con valores indefinidos, es con la función fromkeys()
#dicc = dict.fromkeys("nombre", "apellido")
# Si se deja así, va a iterar el primer elemento, es decir que al momento de mostrarlo aparecería como:
# { 'n': 'apellido', 'o': 'apellido', 'm': 'apellido', 'b': 'apellido', 'r': 'apellido', 'e': 'apellido' }
# Para que no aparezca de esta manera, se hace:
dicc = dict.fromkeys(["nombre", "apellido"])
print(dicc)

# Esos elementos los agarra con la clave(key), y el valor(value) por defecto será None.
# { 'nombre': 'None' } 
# Entonces, el primer valor el que siempre va a iterar, y el segundo es dato que sería el igual,
# que en este caso es None, para cambiar ese valor por defecto se hace: 
dicc = dict.fromkeys(["nombre", "apellido"], "No tiene valor")
print(dicc)