for cont_externo in range(1,6):
    print(f'\nRound {cont_externo}')
    for cont_interno in range(5,0,-1):
        print(f'valor: {cont_interno}')
print('Fim do loop')

import random

for A in range(1,6):
    print(f'\conjunto {A}')
    for B in range(5):
        numero = random.randint(1,100)
        print(f'Valor: {numero}')