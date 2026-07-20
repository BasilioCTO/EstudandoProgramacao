mensagem_1 = "Olá Rachael , como estás ?"
print(mensagem_1)
print("Estou bem")

nome_1 = "Basílio CTO" ; canal = "Darkplay Channel e Dupla Programação"
print(nome_1, "-" ,canal)

nome_2 = str(input("Informe o seu nome: "))
print("Olá "+ nome_2 +" seja bem vinda ao canal Dupla Programação")

print("Imprime a mensagem e muda de linha.")
print("Imprime a mensagem e permanece na linha.",end="")
print("Continuo na mesma linha")

nome_3 = "Basílio CTO" ; idade_1 = 19
mensagem_2 = "Eu sou o {0} e tenho {1}".format(nome_3,idade_1)
print("Eu sou o {0} e tenho {1}".format(nome_3,idade_1))
print(mensagem_2)

nome_4 = "Rachael" ; idade_2 = 17
mensagem_3 = f"Meu nome é {nome_4} e tenho {idade_2}"
print(f"Meu nome é {nome_4} e tenho {idade_2}")
print(mensagem_3)

valor_1 = 10 ; valor_2 = 32
print(f"A soma de {valor_1} com {valor_2} é igual à {valor_1+valor_2}")

valor_3 = 10.3237
print(f"O valor é {valor_3:.2f}")
# Caracteres de escapes \Argumento\ (print("Argumento \"Argumento\"")
# É usado quando queremos imprimir um dado dentro de uma string (Juntamente com uma string)
# Outros caracteres de escapes (\n , \t , \\ ,etc...)
print(f"O valor é \"{valor_3:.2f}\"")

anime = "Tokyo Revange" ; personagem = "Mikey"
print(f"Nome do anime:\t{anime}\tcom a personagem:\t{personagem}")
