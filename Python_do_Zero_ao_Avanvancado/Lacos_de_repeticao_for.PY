# O laço for permite contruir estruturas de repetição pra interação em sequência de dados
# como listas , tuplas , dicionários , etc
# for item in sequência:
#       instrução executadas para cada linha da sequência
# item é o nome da váriavél que o programador cria par ainterar sobre os dados da sequência
# in é o operador de associação
# sequência é o conjunto de valores sobre os quais o programador aplica algum tipo de processo

# Estrutura do laço for e função range() 👇

lista = [10,32,11,35,93]
for item in lista:
    print(item)

palavra = "Rachael"
for letra in palavra:
    print(letra)

for cont_1 in range(11):
    print(cont_1)

nome = input("Informe o seu nome: ")
for cont_2 in range(10):
    print(f"{cont_2+1} {nome}")

# range com 3 paramêtros range(valor_inicial , valor_final , incremento)

for cont_3 in range(10,33,2):
    print(cont_3)

for cont_3 in range(33,10,-2):
    print(cont_3)

nomes = ("Basílio","Rachael","BR")
for cont_4 in nomes:
    if cont_4 == "BR":
        continue
    print(cont_4)