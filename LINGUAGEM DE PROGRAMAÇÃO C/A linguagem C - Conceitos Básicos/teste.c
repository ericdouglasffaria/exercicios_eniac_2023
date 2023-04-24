#include <stdio.h>
#include <stdlib.h>

main()
{
    int idade = 10;

    float salario = 8786.12;

    printf("Digite sua idade: ");
    scanf("%d", &idade);

    printf("Digite o salario: ");
    scanf("%f", &salario);

    printf("AULA 2 \n");
    printf("Sua idade e: %d \n\n\n", idade);

    printf("Salario %09.1f ", salario);

    printf("\n\n\n");

    system("pause");
}
