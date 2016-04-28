

from memoria import *

needed = {'INT' : 5, 'FLOAT' : 1, 'CHAR' : 0, 'BOOL' : 2}

inicial = Memoria('programa', needed)

print(inicial.ints)
inicial.setValorDeDireccion(10001, 5)
inicial.setValorDeDireccion(27501, 123)
print(inicial.bools)
print(inicial.getValorDeDireccion(20000))
