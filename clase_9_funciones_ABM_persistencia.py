import json
import os
#Declaración de funciones

def mostrar_menu():
    print("Operaciones Disponibles:")
    print("1) Cargar usuario por identificador Unico")
    print("2) Buscar usuario por identificador Unico")
    print("3) Borrar usuario por identificador Unico")
    print("4) Modificar usuario por identificador Unico")
    print("5) Salir")


def crear_usuario():
    usuario = input("Usuario: ")
    nombre = input("Nombre: ")
    edad = input("Edad: ")
    password = input("Password: ")
    password_dos = input("Repita el password: ")
    
    usuario_valido = True
    regla_string_usuario_valido = (not usuario[0].isnumeric() and len(usuario) > 6)
    regla_usaurio_no_repetido = (usuario not in usuarios)
    regla_nombre_valido = len(nombre) > 3
    regla_edad_valido = edad.isnumeric()
    regla_password = len(password) > 3 and '#' in password or '%' in password
    regla_repetir_password = password == password_dos
    
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
    

def buscar_usuario():
    criterio = input("Ingrese el Usuario que esta buscando: ")
    resultado = usuarios.get(criterio, "No existe ese Usuario")
    print(resultado)


def borrar_usuario():
    criterio = input("Ingrese el Usuario que esta buscando: ")
    resultado = usuarios.get(criterio, False)
    
    if resultado:
        del usuarios[criterio]
    else:
        print("No existe ese Usuario")

def modificar_usuario():
    criterio = input("Ingrese el Usuario que desea modificar: ")
    resultado = usuarios.get(criterio, False)
    
    if not resultado:
        print("No existe ese Usuario")
    else:
        
        nombre = input("Nombre:")
        edad = input("Edad:")
        password = input("Password: ")
        password_dos = input("Repita el password:")
        
        usuario_valido = True
        regla_nombre_valido = len(nombre) > 3
        regla_edad_valido = edad.isnumeric()
        regla_password = len(password) > 3 and '#' in password or '%' in password
        regla_repetir_password = password == password_dos

                
        if not regla_edad_valido:
            print("Edad tiene que ser un entero")
            usuario_valido = False

        if not regla_password:
            print("EL password tiene que ser mayor a 3 caracteres y tiene que tener un # o %")
            usuario_valido = False
            

        if not usuario_valido:
            print("Corrija los errores")

        else:
            usuarios[criterio] = (nombre, edad, password)
            print(f"Se modificó con éxito el usuario {criterio}")
            print((nombre, edad, password))


def persistir():
    with open("usuarios.json", "w") as archivo:
        archivo.writelines(json.dumps(usuarios, indent=2))



# Inicio de mi script

if __name__ == "__main__":
     
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as archivo:        
            usuarios = json.load(archivo)
    else:
        usuarios = dict()
                  
    while True:
        mostrar_menu()    
        operacion = input("Ingrese operacion: ")
        if operacion == "1":
            crear_usuario()
        elif operacion == "2":
            buscar_usuario()
        elif operacion == "3":
            borrar_usuario()
        elif operacion == "4":
            modificar_usuario()
        elif operacion == "5":
            print("Se sale del programa.")
            break    
        else:
            print("La operación ingresada no existe")
        persistir()      



