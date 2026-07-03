# Os condicionais podem ser (Simples,Compostos,Encadeados,Aninhados)

# Exemplo de condicional simples :
nota_1 = nota_2 = 0.0 ; media = 0
nota_1 = float(input("Insira a primeira nota "))
nota_2 = float(input("Insira a segunda nota "))
media = (nota_1 + nota_2) / 2

if (media >= 7):
    print("Resultado aprovado")
    print("Parabéns")
elif (media >= 5):
    print("Você está de recuperação")
else:
    print("Aluno reprovado")

print("Sua media é {}".format(media))