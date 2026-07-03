media = 32
numero_1 = numero_2 = numero_3 = numero_4 = 0.0
nome , idade = "Basílio","CTO"
estado_1 = True ; estado_2 = False

# Type() nos mostra a classe de uma determinada variavél exemplo(int,str,bool,float,complex) :

print(nome , idade)
print(type(media))
print(type(numero_1))
print(type(nome))
print(type(estado_1))
print(type(estado_2))
print(type(1+2j))

# Isinstace() diz se uma variavél é de um tipo de dado específicado por nós:

dado_1 = 10 ; dado_2 = "Sun"
print(isinstance(dado_1,int))
print(isinstance(dado_2,str))
print(isinstance(dado_1,float))
print(isinstance(dado_2,bool))
print(isinstance(dado_1,(int,float)))

dado_3 = 32 ; dado_4 = 2
resultado = dado_3 * dado_4
print(resultado)