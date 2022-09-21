import math



class punto:
    def __init__ (self, x,y):
        self.x = x
        self.y = y



class recta:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def calcula_longitud(self):
        longitud = math.sqrt((self.b.x-self.a.x)**2+(self.b.y-self.a.y)**2)
        print(longitud)
        
punto_1 = punto(2,5)

punto_2 = punto(6,3)


recta_1 = recta(punto_1, punto_2)


recta_1.calcula_longitud()