diccionario = {
	"nombre": "Pepe",
	"apellido": "Montesco",
	"edad": 34
}

# Iterando un diccionario mostrando solamente sus indices
for key in diccionario:
  print(key)
  
# Iterando un diccionario que muestre el índicie y valor con el método items()
for datos in diccionario.items():
  key   = datos[0]
  value = datos[1]
  print(f'El índice es: {key} y el valor es: {value}')