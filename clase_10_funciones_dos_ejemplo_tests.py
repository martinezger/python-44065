def recortar(num, inferior, superior):
    pass

assert recortar(num=4, inferior=5, superior=8) == 5
assert recortar(num=9, inferior=5, superior=8) == 8
assert recortar(num=7, inferior=5, superior=8) == 7

def separar(numeros_enteros):
    pass

assert separar([1,4,2,5]) == ([2,4], [1,5])
assert separar([1,1,1,1]) == ([], [1,1,1,1])
assert separar([2,2,2,2]) == ([2,2,2,2], [])
assert separar([]) == ([],[])

print("todos los test pasaron")
