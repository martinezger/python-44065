class Punto:
    pass

un_punto = Punto()
un_punto.x = 1
un_punto.y = 1

def print_punto(point):
    print("\tx\ty")
    print(f"\t{point.x}\t{point.y}")
    
    
un_punto = Punto()
un_punto.x = 1
un_punto.y = 1

otro_punto = Punto()
otro_punto.x = 1
otro_punto.y = 1



print(type(un_punto))
print_punto(un_punto)

print("\n\n")

class Recta:
    pass

una_recta = Recta()
una_recta.punto_a = Punto()
una_recta.punto_b = Punto()

una_recta.punto_a.x = 1
una_recta.punto_a.y = 1

una_recta.punto_b.x = 2
una_recta.punto_b.y = 2

def print_recta(recta):
    print_punto(recta.punto_a)
    print_punto(recta.punto_b)

print(type(una_recta))
print_recta(una_recta)


class Punto:
 def __init__(self, x=10, y=0):
   self.x = x
   self.y = y
   
 def print_punto(self, cabecera=True):
   if cabecera:  
       print("\tx\ty")
   print(f"\t{self.x}\t{self.y}")


a = Punto(1,2)

a.print_punto() 


