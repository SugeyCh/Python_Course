# DIR: Es una función que devuelve la lista de atributos válidos del objeto pasado.
# Recibe como parametro que lo toma como objeto, para mostrar por una lista los métodos
# que se pueden trabajar con el objeto que se le esté pasando. Si ponemos un texto, nos muestra lo 
# que podríamos hacer con ese texto.
cadena = "Hola, eres Bienvenido"
"""result = dir(cadena)
print(result) """


# METODOS DE CADENAS: Para aplicar un método, lo que se hace es poner  dato.metodo()

# 1 - UPPER: Convierte todo en mayúscula
mayus = cadena.upper()
#print(mayus)

# 2 - LOWER: Convierte todo en minúscula
minus = cadena.lower()
#print(minus)

# 3 - CAPITALIZATE: Convierte la primera letra en mayúscula
letra_mayus = cadena.capitalize()
#print(letra_mayus)

# 4 - FIND: Busca un valor que se le pida. En este caso, busca una cadena en otra cadena.
# Lo recorre como si fuera un objeto, así que muestra la posición en la que se encuentra.
# En caso de que no consiga nada, devolverá -1
busqueda = cadena.find("a")  #Devuelve que está en la posición 3
#print(busqueda)

# 5 - INDEX: Es igual que find, con la diferencia de que si no consigue nada, 
# lanza una excepción 
busqueda2 = cadena.index("B")
#print(busqueda2)

# 6 - ISNUMERIC: Si es númerico, devuelve True, sino entonces devuelve False.
numerico = cadena.isnumeric()  #Da False porque cadena no tiene ningún número
#print(numerico) 

# 7 - ISALPHA: Si es alfanumerico, dará True, sino dará False.
# Solamente son válidos los carácteres de la a hasta la z. 
# Si la cadena tiene espacios, números, comas y demás cosas, dará False. En cambio, si la cadena 
# fuera: HolaeresBienvenido, Daría True.
alfa = cadena.isalpha()  #Da False
#print(alfa)

# 8 - COUNT: Devuelve el número de ocurrencias de una subcadena en la cadena dada.
# Es decir, en vez de encontrar una coincidencia, nos dice cuántas veces consiguió esa coincidencia.
# Si no encuentra alguna coincidencia, mostrará: 0
coincidencia = cadena.count("e")  #Lanzará el número de veces que se repite esa letra
#print(coincidencia)

# 9 - LEN: Es una función, no un metodo. Lo que hace es que cuenta la cantidad 
# de carácteres que tenga una cadena. Al ser una función se aplica de la siguiente manera:
cantidad = len(cadena)  #Da 21 porque es la cantidad de letras que hay en cadena
#print(cantidad) 

# 10 - STARTSWITH: Verifica si una cadena empieza con otra cadena dada, si es así devuelve True
empieza = cadena.startswith("H")  #Devuelve True porque cadena empieza con H mayúscula, si se pone en minúscula (h),
#print(empieza)                    # da False. Esto es porque Python es sensible a mayúsculas y minúsculas.

# 11 - ENDSWITH: Verifica si una cadena termina con otra cadena dada, si es así devuelve True
termina = cadena.endswith("do")  #Devuelve True porque así termina la cadena, en caso contrario daría False
#print(termina)

# 12 - REPLACE: Reemplaza un valor. A este se le pasan 2 parámetros, el primero es el pedazo de 
# cadena que se desea cambiar, y el segundo es con el nuevo valor
reemplazo = cadena.replace("Hola", "Hey!")  #Ahora en vez de Hola, dirá: Hey!
#print(reemplazo)

# 13 - SPLIT: Separa por un parámetro dado. Separa cadenas con una cadena que se le asigne.
# Devuelve una lista con la separación que le hayamos asignado
separar = cadena.split(",")
print(separar)

# Entonces, como devuelve una lista, entonces se muestra como: ['Hola', 'eres Bienvenido']
# Después de Hola hay una coma que la toma como la separación de cada elemento en la lista, 
# como solamente hay una coma en la cadena, entonces hay 2 elementos en la lista.