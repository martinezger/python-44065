# Checkear si es mayor de 18
edad = 18
if edad >= 18:
    print(f"{edad}, Es mayor de edad")


#Checkear si Es mayor de 18 y es Extranjero (No es Argentino)
edad = 18
pais = "Arg"

if edad >= 18:
    print(f"{edad}, Es mayor de edad")

if not (pais == "Arg"):
    print("Es extrajera")
else:
    print("Es Argentino")
    

#Checkear si es Argetino y si puede comprar Alcohol
edad = 17
pais = "Arg"

if edad >= 18:
  print("Es Mayor a 18.")
  if pais == "Arg":
    print("Puede comprar alcohol.")
  else:
    print("No es Argentino, no puede comprar alcohol")
else:
    print("No es mayot de 18")


#Checkar si Puede votar en Argentina
edad = 16
pais = "Arg"

if edad >= 16 and pais == "Arg":
    print("Puede votar")


#Chekear si es alto
altura = 1.9
if altura > 1.9: 
  print("Es Alto") ## True
else:  
  print("No es Alto") ## False


#Validar nota
nota = 5  
if nota >= 9 :
  print("Sobresaliente")

if nota >= 6 :
  print("BUeno")
else:
  print("Insuficiente")



