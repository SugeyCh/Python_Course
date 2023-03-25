# ENTRADA DE DATA (input)
nombre = input("Ingresa tu nombre: ")
print(nombre)

# Al ingresar el nombre del usuario, la variable nombre pasa a ser automaticamente ese dato 
# que se ingresó. Para ver esto, hacemos un print de nombre. Va a aparecer como:
# Ingresa tu nombre: Pepe
# Pepe

# El dato que va a pedir la función de input, siempre será un texto, si ingresamos un número lo toma como un string.
# Ahora, para pedir números, simplemente se transforma el input en int. Esto lo hacemos:
numero = input("Ingresa un número: ")
result = int(numero) * 3  #El número que se ingrese, lo multiplicará por 3
print(result)

# Y en caso de que se quiera ingresar números flotantes, simplemente se cambia el int, por float