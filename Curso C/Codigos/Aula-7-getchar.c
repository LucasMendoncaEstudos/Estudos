#include <stdio.h>

/*
      Aula 7
  Lendo caracteres
  Função getchar()
*/
int main(void) {

  char letra;
  printf("Digite uma letra: ");
  letra = getchar();

  printf("Caracter lido: %c\n", letra);

  
  return 0;
}