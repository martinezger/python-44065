#Simulador de ABM

while True:
    
    usuario = input("Usuario: ")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    password = input("Password: ")
    password_dos = input("Repita el password: ")


    usuarios = dict()

    regla_string_usuario_valido = (not usuario[0].isnumeric() and len(usuario) > 6)
                            
    regla_usaurio_no_repetido = (usuario not in usuarios)

    regla_nombre_valido = len(nombre) > 3

    regla_edad_valido = edad.isnumeric()

    regla_password = len(password) > 3 and '#' in password or '%' in password

    regla_repetir_password = password == password_dos

    usuario_valido = True

    if not regla_string_usuario_valido:
        print("Usuario: No puede empezar con un Número y Tienen que Ser mayor a 6")
        usuario_valido = False

    if not regla_usaurio_no_repetido:
        print("Usuario ya existe")
        usuario_valido = False
        
    if not regla_edad_valido:
        print("Edad tiene que ser un entero")
        usuario_valido = False

    if not regla_password:
        print("EL password tiene que ser mayor a 3 caracteres y tiene que tener un # o %")
        usuario_valido = False
        

    if not usuario_valido:
        print("Corrija los errores")

    else:
        usuarios[usuario] = (nombre, edad, password)



