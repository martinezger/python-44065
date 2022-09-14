def conversor(*args):
  
  if len(args) == 1:
    horas = args[0] // 3600
    minutos = (args[0] % 3600) // 60
    segundos = (args[0] % 3600) % 60
    
    return horas, minutos, segundos
  
  if len(args) == 3:

    if args[1] > 59:
      return "Minutos no puede ser mayor a 59"
    
    if args[2] > 59:
      return "Segundos no puede ser mayor a 59"

    return args[0] * 3600 + args[1] * 60 + args[2]
  
  return "solo 1 o 3 parametros se pueden usar"

# Pruebo si pasando un parametro anda
assert conversor(3600) == (1,0,0)
assert conversor(60)   == (0,1,0)
assert conversor(1)    == (0,0,1)
assert conversor(3655) == (1,0,55)
assert conversor(3755) == (1,2,35)


# Pruebo si pasando tres parametros anda
assert conversor(1,0,0) == 3600
assert conversor(1,0,55) == 3655
assert conversor(1,2,35) == 3755

# Pruebo cantidad de parametros
assert conversor(1,2) == "solo 1 o 3 parametros se pueden usar"
assert conversor(1,2,3,4) == "solo 1 o 3 parametros se pueden usar"
assert conversor() == "solo 1 o 3 parametros se pueden usar"

# Pruebo minutos y segundos
assert conversor(1,59,0) == 7140
assert conversor(1,0,59) == 3659
assert conversor(1,60,0) == "Minutos no puede ser mayor a 59"
assert conversor(1,0,60) == "Segundos no puede ser mayor a 59"
