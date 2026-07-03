# String é uma sequência de caracter.
# Esses caracteres podem ser números , letras ou qualquer outro digito.
# As strings são imultaveis , ou seja , não se pode alterar

nome_1 = "Dupla" ; nome_2 = "Programação" ; nome_3 = "Darkplay Channel"
canal_do_you_tube = nome_1 + nome_2
print(canal_do_you_tube)
print(len(canal_do_you_tube))
print(canal_do_you_tube[0])

print(nome_3.split())
# O método split converte uma string em lista.
for cont_1 in nome_3.split():
    print(cont_1)

# O método replace é usado para substituir uma string com a outra :
print(nome_3.replace("Channel", "Music"))

# Quando a frase ou srting tem espaços no lugar errado :
frase_1 = " olá , eu sou o steel" # Espaço a esquerda
frase_2 = "olá , eu sou o steel " # Espaço a direita
frase_3 = " olá , eu sou o steel " # Espaço no dois lados
print(frase_1.lstrip())
print(frase_2.rstrip())
print(frase_3.strip())

# Para alinhar uma string usa-se:
frase_1 = " olá , eu sou o steel"
frase_2 = "olá , eu sou o steel "
frase_3 = " olá , eu sou o steel "
print(frase_1.rjust(10))
print(frase_1.ljust(10))

# Para centralizar uma string usa-se:
print(frase_1.center(10))

# Para verificar a inicial de uma string e retorna True or False :
print(frase_1.startswith("o"))
print(frase_1.endswith("l"))

# O find serve para encontrar o índice de um caracter dentro da string:
print(frase_3.find("o"))
# Se o número for negativo , a mensagem será "Caracter não encontrado"

# Upper serve para colocar uma string em maiusculas ou caixa alta:
print(frase_3.upper())

# Upper serve para colocar uma string em minusculas ou caixa baixa:
print(frase_3.lower())

# Capitalize serve para por a primeira letra da frase em maiuscula:
print(frase_2.capitalize())

# Title é usado para por a inicial de cada palavra em maiuscula:
print(frase_3.title())

# Docstrings é uma espécie de documentação que podemos inserir dentro de um módulos
# função ou classe no python , entre outros locais :
# Elas criam-se com 3 aspas(dupla ou simples) podem estar dentro de variaveis , como não !
"""""
Docstrings
"""

Docstring = """""
Docstrings
"""
print(Docstring)
# A primeira docstrings não pode ser visualizada pelo usuario , mas a segunda sim !