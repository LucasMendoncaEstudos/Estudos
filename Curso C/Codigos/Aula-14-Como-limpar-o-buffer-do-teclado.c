#include <stdio.h>


/*
      Aula 14
      Ler dois caracteres
*/
int main(void) {
  char letra1, letra2;
  // leitura do primeiro caracter
  printf("Digite um caracter: ");
  scanf("%c", &letra1);

  // lendo um caracter sem salvar
  scanf("%c");

  printf("Digite outro caracter: ");
  scanf("%c", &letra2);

  printf("O primeiro caracter foi %c\n e o segundo foi %c",letra1, letra2);
  return 0;
}