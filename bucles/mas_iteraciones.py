# Haciendo un recorrido saltandose un valor
frutas = ["fresa", "manzana", "ciruela", "pera", "granada", "mango"]
for fruta in frutas:
  if fruta == 'pera':
    continue
  print(f'Me voy a comer una {fruta}') 
# Al usar continue lo que hace es saltarse ese elemento y seguir con el recorrido

# Para que un bucle no siga ejecutandose, se puede hacer:
for fruta in frutas:
  print(f'voy a comer una {fruta}')
  if fruta == 'pera':
    break
  
print("El bucle se ha terminado")

# El bucle terminado cuando se encuentra con el break, por eso en caso de que se ponga un else en el for,
# tampoco se ejecutaría

# Al mismo tiempo, también se puede recorrer una cadena de texto
saludo = "Bienvenido"
for letra in saludo:
  print(letra)
# Lo que hace es iterar cada una de las letras que tenga la cadena

# Bucles de una sola línea.
numeros = [2, 5, 8, 10]
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)