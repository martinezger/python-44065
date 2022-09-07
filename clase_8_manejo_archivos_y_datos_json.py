import urllib.request
import json

#Rick & Morty Api

# Obtengo un mensaje en formato json desde un servidor
print("====Buscar por Id de personaje=====")
respuesta = urllib.request.urlopen(f"https://rickandmortyapi.com/api/character/1")
body = json.loads(respuesta.read())
print(json.dumps(body, indent=10))

#Guardo el mensaje en formato texto como sample.json
with open("sample.json", "w") as archivo:
    archivo.writelines(json.dumps(body, indent=2))


print("====Buscar por Nombre de personaje=====")
respuesta = urllib.request.urlopen("https://rickandmortyapi.com/api/character/?name=Morty%20Smith")
body = json.loads(respuesta.read())
print(json.dumps(body, indent=2))