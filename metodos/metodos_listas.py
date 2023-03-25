# 1 - LIST: Es una función, no un método, lo que hace es crear una lista
lista = list(["hola", "Pedro", 39])

# 2 - LEN: Es una función que devuelve la cantidad de elementos en una lista
cantidad = len(lista)
#print(cantidad)

# AGREGANDO DATOS A LA LISTA
# 3 - APPEND: Agrega un elemento a la lista
lista.append("Firu")

# 4 - INSERT: Agrega un elemento a la lista en el índice específicado
lista.insert(2, "Mary")  # insert(posición donde se ingresa el nuevo valor, nuevo valor)

# 5 - EXTEND: Agrega varios elementos a la lista. Para poder hacer esto, se hace una lista 
# con los datos nuevos y le especificamos que queremos que esa lista se agregue a la que ya tenemos
lista.extend([True, 2023]) 


# ELIMINANDO DATOS DE LA LISTA
# 6 - POP: Elimina un elemento de una lista, pide índice y devuelve valor
lista.pop(0)  # Eliminó a "hola"
# -1 = elimina el último elemento
# -2 = elimina el penúltimo 
# y así sucesivamente se le puede decir que elimine un elemento.
# Ingresando a su índice, y ponerle un menos a la izquierda

# 7 - REMOVE: Remueve un elemento de la lista por su valor
lista.remove("Mary")

# 8 - CLEAR: Elimina todos los elementos de la lista
#lista.clear()


# ORDENANDO LISTAS
# 9 - SORT: Ordena una lista de forma ascendente o descendente. Esta funciona si tuviera una lista sin strings
lista2 = list([True, False, 2023, 39])
lista2.sort()  #La muestra como: [False, True, 39, 2023] = Ascendente
# Para ver la lista que primero se ordena, y luego la muestre de manera descendente, se hace:
#lista2.sort(reverse=True)  #La muestra: [2023, 39, True, False]
#print(lista2)

# 10 - REVERSE: Invierte los elementos de una lista. La lista puede estar desordenada, 
# pero aún asi ordena los elementos de manera descendente 
lista2.reverse()
#print(lista2)

print(lista)