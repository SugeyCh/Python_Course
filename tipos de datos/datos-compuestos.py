# 1 - LISTA (list)
# Creando una lista (si se pueden modificar los datos)
lista = ["Sugey", "Chacon", True, 1.62]


# 2 - TUPLA (tuple)
# Creando una tupla (no se puede modificar los datos)
tupla = ("Sugey", "Chacon", True, 1.62)

# Al ser una lista, si permite modificar los datos.
lista[1] = "Alviarez"
print(lista[1])

#Al ser una tupla, no permite cambiar los valores y cae en error
#tupla[1] = "Alviarez"
#print(tupla[1])


# 3 - CONJUNTOS
# Creando un conjunto (set).
# No se puede acceder mediante su indice (print(conjunto[1])) ya que dara error,
# No almacena o no puede tener datos duplicados. Al querer verlo, mostrara todos los datos, menos los duplicados
conjunto = {"Sugey", "Chacon", True, 1.62} 

# Tambien, los conjuntos no tienen un orden fijo, son elementos desordenados que pueden cambiar


# 4 - DICCIONARIO
# Creando un diccionario (dict)
# Se hace con formato JSON
diccionario = {
	'nombre': "Sugey",
	'apellido': "Chacon",
  'mayor_edad': True,
  'estatura': 1.62
}

print(diccionario["nombre"]) 
# Para ver sus datos ingresamos a la clave (key).