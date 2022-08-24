#clase 4
"""
Reemplazar por input("mensaje") en la asignación de variables
"""
#Ejercicio Generaciones digitales

fecha_nacimiento = 1945

if 1920 <= fecha_nacimiento <= 1940:
    print("Generación Silenciosa")
elif 1946 <= fecha_nacimiento <= 1964:
    print("Baby Boomer")
elif 1956 <= fecha_nacimiento <= 1979:
    print("Generación X")
elif 1980 <= fecha_nacimiento <= 2000:
    print("Generación Y")
elif 2001 <= fecha_nacimiento <= 2010:
    print("Generación Z")
else:
    print("No existe generación asociada")

#Aprobación Crédito Bancario, super extenso.

edad = 17
antigüedad = 2
ingreso = 4000

mayor_de_edad = edad > 18
antigüedad_minima = antigüedad >= 3
ingreso_minimo_con_antigüedad = ingreso >= 2500
ingreso_minimo_sin_antigüedad = ingreso >=  4000

if mayor_de_edad and antigüedad_minima and ingreso_minimo_con_antigüedad:
    print("Credito aprobado")
elif mayor_de_edad and ingreso_minimo_sin_antigüedad:
    print("Credito aprobado")
else:
    print("credito no aprobado")



#Aprobación Crédito Bancario, Bis short.
    
edad = 17
antigüedad = 2
ingreso = 4000
    
if edad > 18 and antigüedad >= 3 and ingreso >= 2500:
    print("Credito aprobado")
elif edad > 18 and ingreso >=  4000:
    print("Credito aprobado")
else:
    print("credito no aprobado")
    
    
    