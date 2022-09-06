import urllib.request
import json

#Rick & Morty Api


print("====Buscar por Id de personaje=====")
respuesta = urllib.request.urlopen("https://rickandmortyapi.com/api/character/1")
body = json.loads(respuesta.read())
print(json.dumps(body, indent=2))


print("====Buscar por Nombre de personaje=====")
respuesta = urllib.request.urlopen("https://rickandmortyapi.com/api/character/?name=Morty%20Smith")
body = json.loads(respuesta.read())
print(json.dumps(body, indent=2))
