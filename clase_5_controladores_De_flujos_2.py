#Clase 5 Controladores de Flujos 2
lista_a = [1,2,3,4]
lista_b = [1,4,4,7]
salida = []

for a in lista_a:
    for b in lista_b:
        if a == b and a not in salida:
            salida.append(a)

print(f"los repetidos son {salida}")


for a in lista_a:
   if a in lista_b and a not in salida:
       salida.append(a)
       
       
print(f"los repetidos son {salida} 2")
