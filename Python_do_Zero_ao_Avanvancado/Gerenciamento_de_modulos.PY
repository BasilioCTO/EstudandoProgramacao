# Usando apenas o import , estará na nossa disponibilidade o uso de qualquer função da biblioteca
# ou módulo
# Exemplo : import math

# Se usarmos o from nome da biblioteca/módulo import nome da função , estaremos sujeitos a usar
# apenas uma função da biblioteca/módulo importada
# Exemplo : from math import sqrt
# Import universal : from nome do módulo import *
# OBS : Não é recomendado !!
# Atribuindo nome aos módulos : import as nome alternativo

# Podes executar outros códigos dentro de um determinado código da mesma pasta , assim :
# import nome do arquivo ou from nome do arquivo import nome da função

import math
from math import sqrt

print(math.sqrt(81))
print(sqrt(81))

import Variaveis_em_python as vp
if __name__ == '__main__':
    vp

import numpy as np

L = np.array([1,2,3,4,5,6,7,8,9])
print(L)