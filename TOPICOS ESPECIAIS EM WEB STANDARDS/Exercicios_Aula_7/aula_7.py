# montar um programa de equete, onde serão ouvidos N pessoas
# (N é um numero digitado pelo usuário)
# Nessa enquete vai perguntar:
# No final da enquete, o programa deve mostrar:
# seu nome e sua idade.
# quantidade de entrevista
# a media das idades digitadas
# a maior idade digitada
# a menor idade digitada
# ?
# ?
# ?

qtd = int(input("Quantidade de pessoas serem entrevistada: ?"))
contador = 0
soma = 0
maior = 0
menor = 0

while contador < qtd:
    print("------------------------------")
    nome = input(" Digita a seu nome: ")
    idade = int(input(" Digita a sua idade: "))
    if contador == 0:
        maior = idade
    if contador == 0:
        menor = idade

    contador = contador + 1
    soma = soma + idade

    if idade > maior:
        maior = idade
    if idade < menor:
        menor = idade

print("Resultados Esperados:")
print("Quantidades de pessoas entrevista:", qtd)
media = soma / qtd
print("A media das idade digitas foi: ", media)
print("A maior idade digitada:", maior)
print("A menor idade digitada:", menor)
input("Fim da Enquete")
