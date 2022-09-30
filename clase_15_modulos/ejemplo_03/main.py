import sys
from calculos.estructuras import Viga
from calculos.materiales import calcular_hormigon
from calculos.maderas.estructuras import calcular, a, Padre


def main(a, b):
    print(a)
    print(b)
    una_viga = Viga(a,b)
    print(una_viga.calcular())
    print(calcular_hormigon(12))
    print(a)

if __name__ == "__main__":

    a = input("ingrese un numero")
    b = input("ingrese un numero")
    main(int(a),int(b))
   
