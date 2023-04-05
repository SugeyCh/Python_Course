# Creando un conjunto con set()
con = set(["dato1", "dato2"])
#print(con)

# Para poder poner un conjunto dentro de otro conjunto, usamos la función forzenset
con1 = frozenset(["dato 1", "dato 2"])
con2 = {con1, "dato 3"}
#print(con2)

# Hay una teoría de conjuntos, el cual trata de que uno es un conjunto y el otro es un subconjunto.
# El subconjunto vendría teniendo valores igual al otro conjunto. Para verlo de forma práctica es:
con1 = { 1, 3, 5, 7 }
con2 = { 1, 3, 7 }
res  = con2.issubset(con1)
#print(res)

# con1 vendría siendo como un tipo de conjunto principal, del cual se crea el con2 que tiene algunos de los 
# valores que están en con1, con la diferencia de que en con1 hay más datos. Entonces, para saber si un conjunto, 
# es un subconjunto, se aplica la función issubset. Dará True si el conjunto resulta ser un subconjunto, en caso
# contrario, da False. Otra manera para verificar esto es:   res = con2 <= con1

res  = con1.issuperset(con2)
res1 = con2 > con1
#print(res)

# Un superconjunto, vendría siendo que con1 sea este superconjunto de con2. Al ser así, res dará True, porque 
# con1 es un superconjunto de con2, y en res1 dará False porque con2 no lo es. con1 tiene datos similares que con2, 
# pero, aparte de esos datos, tiene otros que con2 no tiene. La función issuperset es para saber si un conjunto es 
# un superconjunto

res = con2.isdisjoint(con1)
print(res)

# isdisjoint es para verificar si tiene algún número en común. Esta función dará True sólo cuando los datos no sean 
# similares, si posee aunque sea un dato similar, dará False