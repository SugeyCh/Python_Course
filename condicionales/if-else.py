# CONDICIONALES
# Son pedazos de código que se ejecutan en caso de que un procedimiento sea verdadero. 
# Si la condicional es verdadera, ejecutará un bloque de código, 
# sino, entonces no se ejecuta o se le indica que corra otro bloque de código

# (si) if condicion que se cumple: True
#    código a ejecutar en caso de que sea cierto
# (de lo contrario) else: False
#    código a ejecutar en caso de que sea falso

edad = 16
if edad >= 18:
  print("Puedes pasar")
else:
  print("Sos menor, no puedes pasar :(")  
  
# Python al ser un lenguaje identado, tomará todo lo que
# se ponga dentro del if, y de la manera en que se puede salir del bloque de código,
# es borrando la identación que por defecto da al darle Enter dentro del if o el else

clave_usuario = "Pepe123"
clave_escrita = "pepe123"

if clave_usuario == clave_escrita:
  print("Iniciando Sesión...")
else:
  print("Clave incorrecta, intente de nuevo")