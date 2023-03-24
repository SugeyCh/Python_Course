# OPERADORES DE COMPARACION
#  ==  igual que
#  !=  distinto de
#  <   menor que
#  <=  menor o igual que
#  >   mayor que
#  >=  mayor o igual que

igual = 5 == 7  # False
disti = 5 != 7  # True
menor = 5 <  7  # True
me_ig = 5 <= 7  # True
mayor = 5 >  7  # False
ma_ig = 5 >= 7  # False

# Estos operadores de comparación devolveran True o False
#print(ma_ig)


# Ejemplo
a   = 5
b   = 10
c   = 15
res = a + b == c
print(res)
# a + b = 15. c = 15. Entonces, el resultado de a + b, es igual que (==) c, dará True, sino entonces dará False

clave_user = "Pepe123"
clave_escr = "pepe345"
print(clave_user == clave_escr)
# Dará False porque son distintas, además de que hay que recordar que python es sensible con las mayúsculas y minúsculas
# por lo que si pusieramos:
clave_usuario = "Pepe123"
clave_escrita = "pepe123"
print(clave_usuario == clave_escrita)  # Seguirá dando False