#include <stdio.h>
#include <stdlib.h> 

/*
      Aula 9
  Lendo caracter
  Função fgetc()
*/


int main(void) {
  char letra;

  printf("Digite um caracter: ");
  letra = fgetc(stdin);
  printf("O caracter digitado foi : %c\n", letra);
  return 0;
}