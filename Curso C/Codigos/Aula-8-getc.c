#include <stdio.h>
#include <stdlib.h>

/*
      Aula 8
  Lendo caracteres
  Função getc()
*/
int main(void) {
  char letra;

  printf("Digite um caracter: ");
  letra = getc(stdin);
  printf("Caracter lido: %c\n", letra);
  
  
  return 0;
}