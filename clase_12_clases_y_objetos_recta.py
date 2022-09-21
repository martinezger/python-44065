import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        

class Recta:
    def __init__(self, punto_a, punto_b):
        self.punto_a = punto_a
        self.punto_b = punto_b
        
    def calcular_longitud(self):
        x1 = self.punto_a.x
        y1 = self.punto_a.y
        
        x2 = self.punto_b.x
        y2 = self.punto_b.y
        
        return math.sqrt((x2-x1)**2+(y2-y1)**2)