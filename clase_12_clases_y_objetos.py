import turtle as t
import math

def cuadrado(lado=100):
    t.fd(lado)
    t.rt(90)
    t.fd(lado)
    t.rt(90)
    t.fd(lado)
    t.rt(90)
    t.fd(lado)
    t.rt(90)

def cuadrado_dos(lado=100):
    t.bk(lado)
    t.rt(90)
    t.bk(lado)
    t.rt(90)
    t.bk(lado)
    t.rt(90)
    t.bk(lado)
    t.rt(90)
    
def triangulo(cateto_a=100, cateto_b=100):
    t.fd(cateto_a)
    t.rt(90)
    t.fd(cateto_b)
    t.rt(135)
    t.fd(math.sqrt(cateto_a**2+cateto_b**2))


def circulo(circunferancia):
    pass