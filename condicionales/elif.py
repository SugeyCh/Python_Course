# El else if, como se conoce en JavaScript, trabaja en la misma condicional que el 
# if principal, es decir, que siga siendo True pero con otro tipo de procedimiento.
# Trabaja en caso de que no cumpla exactamente con toda la condicional, pero que aún asi es cierta.
# Permite condicionar la ejecución de uno o varios bloques de sentencias al cumplimiento de una o varias condiciones
# En python se usa como: elif

""" salario_mensual = 5000

if salario_mensual > 10000:
  print("Tienes mucho dinero!")
elif salario_mensual > 1000:
  print("Tienes un buen pago")
else:
  print("No tienes mucha paga") """
  
# Tambien se puede hacer con if anidados
salario = 81000
gasto   = 80000

if salario > 10000:
  if salario - gasto < 0:
    print("No tienes fondos")
  elif salario - gasto > 2000:
    print("Vas bien")
  else:
    print("Estas gastando mucho")
else:
  print("No ganas mucho")