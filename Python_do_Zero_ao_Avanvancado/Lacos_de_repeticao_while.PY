# O laço while serve para repetir um bloco de codigos mais de 1 vez
# E tem como caracteristica como sendo uma estrutura de repetição usada quando não sabemos
# o número de repetições a ser feita
# None é uma variavel em python que significa "nada ou vazio"

# Estrutura do laço While 👇

numero = 1
while (numero <= 10):
    print(numero)
    numero += 1
print("Laço encerrado!")

nome = None
while True:
    print("Escreva o seu nome , ou x para parar: ")
    nome = input()
    if nome == 'x' or nome == "X":
        break
    print(f"Bem-vindo, {nome}")
print("Até logo")