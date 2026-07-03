# As tuplas são imutáveis , quer dizer que não se pode alterar o conteúdo da tupla
# depois da criação. E usa-se "()" para declarar as tuplas.
# Pode se acessar os valores da tupla usando indice.

inicias = ('B','R','V','E','M','A')
numeros = (10,23,32,35,39,93,99)
concatenacao_das_tuplas = inicias + numeros
print(concatenacao_das_tuplas)
print(concatenacao_das_tuplas[0])
print(concatenacao_das_tuplas[-1])
print(concatenacao_das_tuplas[:2])
print(concatenacao_das_tuplas[-2:])
print(concatenacao_das_tuplas.count('B'))# O count conta quantas vezes um elemento aparece na tupla
# As operções são quase iguais em relação as listas

# Métodos que não se deve usar nas tuplas :
# Sort() , Append() , Reverse() , pop() , todos os métodos que alteram a tupla são proibidos.