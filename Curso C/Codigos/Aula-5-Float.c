#include <stdio.h>
#include <stdlib.h>

/*
      Aula 5
  Lendo números reais
*/
int main(void) {

  // tipo nome
  float numero = 3.1415;

  printf("Valor da minha variavel: %f\n", numero);

  printf("Digite um número real: ");
  scanf("%f", &numero);

  printf("Valor lido: %.3f", numero);
  
  
  return 0;
}