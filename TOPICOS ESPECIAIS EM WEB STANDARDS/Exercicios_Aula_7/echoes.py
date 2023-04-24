import math

quantity = int(input("Quantas pessoas serão entrevistadas? "))

ages = []
names = []

for i in range(quantity):
    name = input("Qual o seu nome? ")
    names.append(name)

    if (not len(name)):
        print("Invalid name.")

    age = int(input("Qual a sua idade? "))
    ages.append(age)


print(f"Quantidade de pessoas entrevistadas: {quantity}")

avarageAge = math.fsum(ages) / len(ages)
greaterAge = max(ages)
lowerAge = min(ages)

for i in range(len(names)):
    print(f"Name: {names[i]}\n Age: {ages[i]}")

print(f"Average Age: {avarageAge}")
print(f"Greater Age: {greaterAge}")
print(f"Lower Age: {lowerAge}")
