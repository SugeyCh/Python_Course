# DATOS:
# Este curso: 1.5h
# Mínimo: 2.5h
# Máximo: 7h
# Promedio: 4h

# A - Diferencia de porcentaje entre el curso actual y:
# - el más rápido de otros cursos
# - el más lento de otros cursos
# el promedio de los cursos

# Promedio de duración
otros_cursos_min  = 2.5
otros_cursos_max  = 7
otros_cursos_prom = 4
este_curso        = 1.5

# Diferencia de duración:
diferencia_min  = 100 - este_curso / otros_cursos_min * 100
diferencia_max  = 100 - este_curso * 1000 // otros_cursos_max / 10
diferencia_prom = 100 - este_curso / otros_cursos_prom * 100

# Mostrando las diferencias de duración (Parte A)
print('--------------------------')
print(f'Este curso dura un {diferencia_min}% menos que el más rápido')
print(f'Este curso dura un {diferencia_max}% menos que el más lento')
print(f'Este curso dura un {diferencia_prom}% menos que el promedio')


# B - Porcenaje de material inservible que se reduce en:
# - el promedio de los cursos
# - el curso actual
 
# Calculando el porcentaje de tiempo vació o material innecesario en un vídeo
vacio_promedio = 5
vacio_curso    = 3.5

tiempo_vacio_promedio = 100 - otros_cursos_prom * 1000 // vacio_promedio / 10
tiempo_vacio_curso    = 100 - este_curso * 1000 // vacio_curso / 10

# Mostrando la cantidad de espacios vacíos que se remueven (Parte B)
print('--------------------------')
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacío')
print(f'Este curso eliminó el {tiempo_vacio_curso}% de tiempo vacío')
print('--------------------------')


# C - Ver 10 horas de este curso a cuantas de otros equivale? ¿y al revés?
# Mostrando diferencias si los cursos duraran 10 horas (Parte C)
print(f'Ver 10 horas de este curso equivale a ver {otros_cursos_prom * 100 // este_curso / 10} horas de otros cursos')
print(f'Ver 10 horas de otros cursos equivale a ver {este_curso * 100 // otros_cursos_prom / 10} horas de este curso')
print('--------------------------')