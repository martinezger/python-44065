class Persona:
    pass

pedro = Persona()
juan = Persona()
juancito = juan

class Persona:
  idioma = "Castellano" # Atributo de clase - afecta a todas
                            # las instancias/objetos
  
  def __init__(self, nombre, apellido):
    self.nombre = nombre # Atributo de instancia/objeto,
                         # solo afecta a la instancia.
    self.apellido = apellido
  
  def print_idioma(self):
    print(Persona.idioma)
                                    

  def presentarse(self):
    if Persona.idioma.lower() == "castellano":
      print(f"Hola Soy, {self.nombre}, {self.apellido}")
    elif Persona.idioma.lower() == "portugues":
      print(f"Eu sou, {self.nombre}, {self.apellido}")


'''
Recordar que para poder utilizar dateutil en thonny hay que instalarlo primero
mediante el manejador de plugins. La libreria se llama: py-dateutil
'''

import datetime
from dateutil.relativedelta import relativedelta

class Persona:
  __idioma = "Castellano" # Atributo de clase - afecta a todas - Modo Privado
                            # las instancias/objetos
  
  def __init__(self, nombre, apellido, fecha_nacimiento):
    self.nombre = nombre # Atributo de instancia/objeto,
                         # solo afecta a la instancia.
    self.apellido = apellido
    self.__fecha_nacimiento = fecha_nacimiento #  Modo Privado

  
  def print_idioma(self):
    print(Persona.__idioma) #  Name mangling - Modo Privado
                                    

  def presentarse(self):
    print(f"Hola Soy, {self.nombre}, {self.apellido} y tengo {self.edad}")
  
  @property
  def edad(self):
    return relativedelta(datetime.date.today(), self.__formatear_fecha_nacimiento()).years
  
  def __formatear_fecha_nacimiento(self):
      return datetime.datetime.strptime(self.__fecha_nacimiento, "%d/%m/%Y")
    
  def print_self(self):
    print(self)
