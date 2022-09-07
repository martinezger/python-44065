import json

archivo_texto = open("guia_telefonos.json", "w")

contenido = """{

  "usuario_1": {
    "nombre": "German",
    "Apellido": "Martinez",
    "Telefonos": [
      "555-1234","555-9876"
    ]
  },

  "usuario_2": {
    "nombre": "Raul",
    "Apellido": "Martinez",
    "Telefonos": [
      "555-1234","555-9876"
    ]
  }

}"""

archivo_texto.write(contenido)
archivo_texto.close()


archivo_texto = open("guia_telefonos.json", "r")

for reglon in archivo_texto:
  print(reglon)

archivo_texto.close()

'''
archivo_texto = open("guia_telefonos.json", "a")

archivo_texto.write("\nESCRIBO ALGO EN EL FILE")
archivo_texto.close()
'''

archivo_texto = open("guia_telefonos.json", "r")
guia_telefonos = json.load(archivo_texto)



