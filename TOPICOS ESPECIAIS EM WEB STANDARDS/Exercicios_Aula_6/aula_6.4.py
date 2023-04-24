# montar um programa que o usuário digita um número e o computador irá somar
# todos os números entre 1 até o número digitado.
# obs.: O número digitado pode ser positivo ou negativo.

# 3
# 1 + 2 + 3 = 6

# -3
# 1 + 0 + (-1) + (-2) + (-3) = -5

numero = int(input(" Digita um numero: "))

contador = 1
soma = 0

if numero > 0:
    while contador <= numero:
        soma = soma + contador
        contador = contador + 1
    print("A soma dos numeros de um ate ", numero, " é:", soma)
    print("Numero positivo")
else:
    while contador >= numero:
        soma = soma + contador
        contador = contador - 1
    print("A soma dos numeros de zero um ", numero, " é:", soma)
    print("Numero negativo")

input("Digita tecla para, Fim do Programa")
