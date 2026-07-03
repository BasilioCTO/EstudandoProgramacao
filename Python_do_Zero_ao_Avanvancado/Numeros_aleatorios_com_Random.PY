# Para trabalhar com números aleatórios , usa-se o random , um metódo do python
# e significa "Aleatório"
# Randint é usado para números aleatórios do tipo inteiro
# uniform é usado para números aleatórios do tipo decimal
# O random.random gera um número aleatório entre 0 e 1

import random
valor_aleatorio_1 = random.randint(10,32)
print(valor_aleatorio_1)

print("Gerar números aleatórios entre 10 e 32")
for cont_1 in range(10,32):
    numero_aleatorio_2 = random.randint(10,32)
    print(f'Número gerado: {numero_aleatorio_2}')

valor_aleatorio_3 = random.random()
print(round(valor_aleatorio_3*10,2))
# valor_aleatorio_3 * 10 , faz com que muda a escala em que serão gerados os valores
# Round é uma função qualquer que arredonda um número

valor_aleatorio_4 = random.uniform(10,32,39,93)
print(round(valor_aleatorio_4,2))

numero_escolhido_1 = random.choice([10,32,37])
print(f"Número escolhido {numero_escolhido_1}")
# A função choice é integrada no metodo Random , e serve para escolher um dado entre vários.

lista_numerica = [10,32,37,39,93]
numero_escolhido_2 = random.sample(lista_numerica,2)
print(f"Os dois números escolhidos são {numero_escolhido_2}")
# A função sample é integrada do método Random , e serve para escolher um determinado dado
# entre vários , e retorna uma lista com os mesmo dados.

print(f"Lista embaralhada {random.shuffle(lista_numerica)}")
# A função shuffle é integrada do método Random , e serve para embaralhar uma lista , e retorna
# a lista embaralhada.