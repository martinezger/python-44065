import csv

# Escritura de CSV append.
while True:

    usuario = input("Ingrese Usuario: ")
    nombre = input("Ingrese nombre: ")
    fecha_nacimiento = input("Ingrese fecha nacimiento (29/02/1997): ")
    
    # Cargo el csv
    with open("sample.csv", "a") as archivo:
        archivo = csv.writer(archivo, delimiter=',')
        archivo.writerow([usuario, nombre, fecha_nacimiento])
    
    if input("cargar otro s/n") == "n": break
    
    
# Muestro el csv
with open("sample.csv") as archivo:
    for linea in archivo:
        print(linea)

#Actualizo
usuario = input("Ingrese usuario para actulizar:")

with open("sample.csv") as archivo:
    readFile = csv.reader(archivo)
    updated_file = []
    for linea in readFile:
        if linea[0] == usuario:
            linea[1] = input("Ingrese Nuevo Nombre: ")
            linea[2] = input("Ingrese Nueva Fecha Nacimiento: ")
        updated_file.append(linea)

with open("sample.csv", "w") as archivo:
    writeFile = csv.writer(archivo)
    writeFile.writerows(updated_file)

# Muestro el csv actualizado
with open("sample.csv") as archivo:
    for linea in archivo:
        print(linea)
        
