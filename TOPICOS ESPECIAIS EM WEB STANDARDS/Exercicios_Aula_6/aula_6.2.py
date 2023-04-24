# montar um programa que usuario digita o seu nome e a quantidade de linhas e mostra 5 vezes.
# (utilizando a estrutura de repetição while)

nome = input("Digita o seu nome?")
qtd = int(input("Digita quantas vezes para repetir seu nome?"))
contador = 0

while contador < qtd:
    print("O nome digitado foi: ", nome)
    contador = contador + 1
input("Digita tecla para, Fim do Programa")
