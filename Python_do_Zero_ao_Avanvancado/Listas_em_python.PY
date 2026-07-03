# Lista representa uma sequência de valores armazenados na memória do computador
# Ela suporta vários tipos de dados em uma só vez.

lista_numerica = [10,32,35,39,75,93]
print(lista_numerica)

# Concatenação de lista , significa juntar duas listas usando o sinal "+" :

lista_numerica_1 = [10,32,35,39,75,93]
lista_numerica_2 = [10,32,35,39,75,93]
concatenacao_das_duas_listas = lista_numerica_1 + lista_numerica_2
print(concatenacao_das_duas_listas)

# Uso do método slicing para acessar valores usando indice positivo:
print(concatenacao_das_duas_listas[5])

# Uso do método slicing para acessar valores usando indice negativo:
print(concatenacao_das_duas_listas[-1])

# O -1 acessa o último elemento da lista
# Ou seja , para acessar valores do último ao primeiro , começa-se do -1,-2,-3... assim por diante
# Atribuir valores a um indice específico usando o slicing:

# concatenacao_das_duas_listas[10] = 99
# print(concatenacao_das_duas_listas[10])

# Método slicing para acessar multiplos valores da lista Lista[valor inicial:quantidade de valores]
# Lista[:quantidade de valores] : Mostra desde o primeiro até a quantidade específicada.
# Lista[valor inicial:] : Mostra desde o primeiro até ao último.
# Lista[valor inicial : fim : critério] ou Lista[::] : é a mesma coisa só que mais controlada

print(concatenacao_das_duas_listas[0::])
print(concatenacao_das_duas_listas[0:])

# Achando a quantidade de elementos da lista usa-se o len().len(lista):
print(len(concatenacao_das_duas_listas))
# Ordenar a lista usa-se o sorted.sorted(lista)
print(sorted(concatenacao_das_duas_listas))
print(sorted(concatenacao_das_duas_listas,reverse=True)) # Ordem decrescente.
print(sum(concatenacao_das_duas_listas)) # Soma os valores da lista.
print(max(concatenacao_das_duas_listas)) # Acha o maior da lista.
print(min(concatenacao_das_duas_listas)) # acha o menor da lista.

# Append serve para acrescentar valores a lista. lista.append(valor)
concatenacao_das_duas_listas.append(23)
# Pop serve para tirar o elemento da lista. lista.pop(indice/vazio)
concatenacao_das_duas_listas.pop()
# Insert serve para inserir elementos na lista. lista.insert(indeice,valor)
concatenacao_das_duas_listas.insert(0,23)