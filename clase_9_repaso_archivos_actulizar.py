import json

a = open("actualizar.txt", "w")
a.write("primer renglon\nsegundo renglon\ntercer renglon")
a.close()

a = open("actualizar.txt", "r")
for renglon in a:
    print(renglon)
    
a.close()

a = open("actualizar.txt", "r")
nuevo_archivo = []

for renglon in a:
    if "segundo" in renglon:
        nuevo_archivo.append("2do reglon\n")
    else:
        nuevo_archivo.append(renglon)
        
a.close()

a = open("actualizar.txt", "w")

for reglon in nuevo_archivo:
    a.write(reglon)

a.close()


a = open("actualizar.txt", "r")
for renglon in a:
    print(renglon)
    
    
archivo_texto = open("guia_telefonos.json", "w")

# cuando en python se usa triple comilla es que se va a usar texto multi linea.

contenido = """{

  "usuario_1": {
    "nombre": "German",
    "Apellido": "Martinez",
    "Telefonos": [
      "555-1234","555-9876"
    ]
  },

  "usuario_2": {
    "nombre": "German",
    "Apellido": "Martinez",
    "Telefonos": [
      "555-1234","555-9876"
    ]
  }

}"""

archivo_texto.write(contenido)
archivo_texto.close()   
    

archivo_texto = open("guia_telefonos.json", "r")


mi_guia_dict = json.load(archivo_texto)

archivo_texto.close()

mi_guia_dict["usuario_2"]["nombre"] = "Raul"

archivo_texto = open("guia_telefonos.json", "w")
archivo_texto.write(json.dumps(mi_guia_dict))
archivo_texto.close()

   
    
    
    
    