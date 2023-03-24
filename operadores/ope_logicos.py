# OPERADORES LOGICOS (algunos de ellos)
# 1 - AND (&): Compara entre un valor y el otro, y sólo devuelve True si ambas condiciones son ciertas, 
# si una de ellas es True y la otra False, al tener un solo valor falso, devolverá todo como False.
resul  = True  & True  #Devuelve True. Ambas condiciones son ciertas.
resul2 = True  & False #Devuelve False. Una de ellas es falsa, así que todo el proceso lo convierte en False.
resul3 = False & False #Devuelve False


# 2 - OR (|): Devolverá False si ambas condiciones son falsas, si una de ellas es True, seguirá con 
# el proceso y convertirá todo el True. Es lo contrario que AND(&).
resul4 = True  | True  #Devuelve True
resul5 = False | True  #Devuelve True. Uno de los valores es cierto, así que todo lo convierte en True
resul6 = False | False #Devuelve False. Ambas condiciones son falsas


# 3 - NOT: Invierte un valor, es decir que da el valor contrario a lo que le estemos pasando
resul7 = not True  #Invierte el valor y da False
resul8 = not False #Invierte su valor y da True

print(resul8)