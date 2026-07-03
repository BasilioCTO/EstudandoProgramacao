# No python existem funções matemáticas internas ou buin e funções
# via módulo

# Funões buin são funções que já existem no python e não é necessário importar 
# nada nem um módulo qualquer.

# Funções via módulo são funções que para ser usadas é necessário importar um módulo , ex.: math

# Aviso , preste só atenção nas funções internas usadas nos códigos !
# Códigos de exemplos com funções buil :

valor_1 = 10 ; valor_2 = -10 ; valor_3 = 10.3293
lista_numerica_1 = [10,32,35,39,75,93]
lista_numerica_2 = [10,32,35,39,75,93]
concatenacao_das_duas_listas = lista_numerica_1 + lista_numerica_2

print(abs(valor_2))
# A função abs retorna o valor absoluto das variaveis.
print(pow(valor_1,2))
# A função pow retorna a potência de um número , ex.: pow(numero,expoente)
print(sum(concatenacao_das_duas_listas)) # Soma os valores da lista.
print(max(concatenacao_das_duas_listas)) # Acha o maior da lista.
print(min(concatenacao_das_duas_listas)) # acha o menor da lista.
print(round(valor_3,2))

# Códigos de exemplos com funções via módulos , ex.: math :
import math as m

valor_4 = 100 ; valor_5 = 1024 ; valor_6 = 10
print(m.sqrt(valor_4))
print(m.sqrt(valor_5))
# O ceil é usado para arredondar um número para cima ou um inteiro a mais , ex.: de 2,8009 à 3
print(m.ceil(m.sqrt(valor_4)))
# O floor é usado para arredondar um número para baixo ou um inteiro a menos , ex.: de  3 à 2
print(m.floor(m.sqrt(valor_4)))

# Logaritimo é um valor ao qual nos elevamos um número , para obter um determinado número
# Ex.: log10 de 100 = 2 , porque 10 elevado a 2 é 100 !
print(m.log10(valor_6))
# Constantes no módulo math :
print(round(m.pi,2))
# Fatorial no módulo math :
print(m.factorial(valor_6))
# inf é um valor do infinito:
print(valor_6 / m.inf)