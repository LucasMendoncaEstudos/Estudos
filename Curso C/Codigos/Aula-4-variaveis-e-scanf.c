#include <stdio.h>
#include <stdlib.h>

/*
      Aula 4
  Lendo números inteiros
*/
int main(void) {

  int valor,valor1, valor2; // Criei uma variavel para guardar um valor do tipo inteiro
  //Atribuição -> atribuir um valor a uma variável
  valor = 50;
  printf("O primeiro valor é :%d", valor);
  printf("\nDigite um valor inteiro: ");
  scanf("%d", &valor1);
  printf("Digite um segundo valor inteiro: ");
  scanf("%d", &valor2);
    printf("\nPrimeiro valor: %d\nSegundo valor: %d", valor1, valor2);
  return 0;
}