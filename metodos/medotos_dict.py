diccionario = {
	"nombre": 'Firu',
	"edad": 39,
	"genero": 'Masculino'
}

# 1 - KEYS: Devuelve las claves. Recordar que un diccionario es un jason y está con la estructura de:  key: value
clave = diccionario.keys()  # Devuelve una lista con los índices del diccionario
#print(clave)         # dict_keys(['nombre', 'edad', 'genero'])

# 2 - GET: Devuelve el valor de una clave
valor = diccionario.get("nombre")
#print(valor)
# Ingresamos el valor de la key y nos mostrará su valor.
# Otra manera de hacerlo es: 
#valor = diccionario["nombre"]
# Si se hace de esta manera, y se le ingresa una key que no existe, cae en error y el programa deja de funcionar, 
# lo cual no sucede con get(), ya que si se le ingresa un elemento que no existe, simplemente manda "none", y 
# el programa sigue funcionando

# 3 - CLEAR: Elimina todos los elementos del diccionario.
#diccionario.clear() 
#print(dicc)

# 4 - POP: Elimina un elemento.
z = diccionario.pop("nombre")
#print(z)
#print(diccionario)

# 5 - ITEMS: Es para iterar el diccionario.
iterar = diccionario.items()  #Devuelve el diccionario de una manera que se pueda iterar: 
print(iterar)                 # ([('edad', 39), ('genero', 'Masculino')])