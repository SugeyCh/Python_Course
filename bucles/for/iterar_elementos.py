# BUCLE FOR
# Repite de forma controlada la ejecución de un código.
# El bucle for permite iterar un elemento (listas, tuplas, diccionarios, conjuntos, etc).
# Iterar es recorrer un elemento en pedazos.

animales = ["gato", "perro", "tucán", "pingüino"]
for animal in animales:
  print(animal)  
  
# ¿Qué valor va a tener animal?: Va a ser igual al valor del primer elemento de la lista animales, luego hace 
# un recorrido y esta vez tendrá el valor del segundo elemento de la lista. Termina de ejecutarse cuando haya 
# llegado al último elemento.

numeros = [52, 16, 14, 72]
for numero in numeros:     # Lo que hace es agarrar cada uno de los elementos de la lista,
  res = numero * 10        #  para multiplicarlos por 10
  print(res)

# ¿Cómo se puede iterar 2 o más listas al mismo tiempo?
# Se puede poner un for dentro de otro for (for anidados). Pero la mejor manera de hacerlo es con una función zip()
for numero,animal in zip(numeros, animales):
  print(f'Esta es la lista de los números: {numero}')
  print(f'Esta es la lista de los animales: {animal}')
  
# Para recorrer una lista con su índice se usa la función enumerate()
for num in enumerate(numeros):
  indice = num[0]
  valor  = num[1]
  print(f'El indice es: {indice} y el valor es: {valor}')
  
# Otra punto a recalcar en los bucles for, es que se puede usar else
for numero in numeros:
  print(f'Este es el último bucle de ejemplo que se va a ejecuta, con valor de: {numero}')
else:
  print('el bucle terminó')

# Al poner el else, se pone a la misma altura o identación que tiene for. 

# Todo esto funciona igual tanto para: listas, tuplas y conjuntos