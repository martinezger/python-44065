# Concat <-- esto es un comentario en el codigo, no se interpreta.

datos = [1, -5, 123,34, 'Una cadena', 'Otra cadena']

print(datos)

print(datos + [0, 'Otra cadena distinta', 'Pepito', -873758,123])

print(datos)

# Mutable e Inmutable

cadena_de_caracteres = "Hola"
#cadena_de_caracteres[0] = "h"

lista_de_caracteres = ["H","o","l","a"]
lista_de_caracteres[0] = "h"

# Slicing
lista_de_algo = ["H","o","l","a", 1 ,2, 3, 7, 8,  [1,2]]
print(lista_de_algo[0: -1]) # del primero al ante último

numeros = [0,1,2,3,4,5,6]
numeros[:3] = ["a","b",77]


# Append

a = []

b = 1

a.append(b)

a.append(1)

a.append(2)


a.append(3+5) # 8

# Pop

print(a.pop() + 10)
      

a = [[[[[[[1]]]]]]]
# Tuplas

tupla_num = (1,2,3,4,)

lista_anidada = [1 ,2 ,[3,4]]

tupla_anidada = (1,2,3,4,(1,2,), [1,2])