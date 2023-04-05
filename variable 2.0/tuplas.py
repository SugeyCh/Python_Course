# Creando una tupla con la función tuple que recibe como parametro una lista
tupla = tuple(["dato1", "dato2"])

# Otra manera para hacer una tupla es:
tupla = "dato1", "dato2"  # Si se ponen los datos separados por un coma, automaticamente lo toma como una tupla
tupla = "dato1",          # Y en caso de que se quiera poner un solo dato en la tupla, se pone una coma al final
print(tupla)

# ¿Cuándo se debe de usar las tuplas?
# Se usa solamente cuando vayamos a poner algo que sea de solo lectura, ya que las tuplas no se puede
# modificar como las listas, ya que se corre el reisgo de que se pierdan esos datos, en cambio en una listas 
# se pueden modificar los datos porque las listas son modificables, las tuplas no