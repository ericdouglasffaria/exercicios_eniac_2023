# Montar um programa de enquete, onde serão ouvidos N pessoas (o programa deve perguntar se deseja continuar as entrevistas). Nesta enquete será perguntado o seu nome, a sua idade e o seu sexo (M, F, O). No final da enquete, o programa deve mostrar:
# a) Quantidade de Entrevistados
# b) A média das idades digitadas
# c) A maior idade digitada
# d) A menor idade digitada
# e) Quantidade de pessoas do sexo Feminino
# f) Quantidade de pessoas do sexo Masculino
# g) Quantidade de pessoas do sexo Outros
# h) Porcentagem de pessoas dos sexos


continua = "sim"
contador = 0
soma = 0
maior = 0
menor = 0
contF = 0
contM = 0
contO = 0
porcF = 0
porcM = 0
porcO = 0

while continua == "sim" or continua == "SIM":
    print("-------------------------------------------")
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo (F, M ou O) : ")

    if contador == 0:  # variavel maior irá receber o valor da
        maior = idade  # idade (if)
        menor = idade
    contador = contador + 1
    soma = soma + idade
    if idade > maior:       # se o usuario digitou uma idade maior
        maior = idade
    if idade < menor:
        menor = idade
    if sexo == "f" or sexo == "F":
        contF = contF + 1
    elif sexo == "m" or sexo == "M":
        contM = contM + 1
    else:
        contO = contO + 1

    continua = input("Deseja continuar a entrevista ? (SIM ou NÃO): ")

print("-------------------------------------------")
print("Resultados")

print("Quantidade de pessoas entrevistadas: ", contador)
media = soma / contador
print("A média das idades digitadas foi: ", media)
print("A maior idade digitada é: ", maior)
print("A menor idade digitada é: ", menor)
print("A quantidade de pessoas do sexo Feminino : ", contF)
print("A quantidade de pessoas do sexo Masculino: ", contM)
print("A quantidade de pessoas do sexo Outros   : ", contO)
porcF = contF * 100 / contador
print("A porcentagem de pessoas do sexo Feminino : ", porcF)
porcM = contM * 100 / contador
print("A porcentagem de pessoas do sexo Masculino : ", porcM)
porcO = contO * 100 / contador       # porcO = 100 - (porcF + porcM)
print("A porcentagem de pessoas do sexo Outros: ", porcO)
input("Fim da Enquete")
