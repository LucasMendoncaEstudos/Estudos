#include <stdio.h>

/*
      Aula 17
  Operador short para o tipo int
  intervalo: -32.768 ate 32.767 pode ser utilizado o short int
  %hi ou %d

*/
int main(void) {
  int y = 0;
  short int x = 32767;

  printf("Tamanho de um int na memoria: %d bytes\n", sizeof y);
  printf("Tamanho de um short int na memoria: %d bytes\n", sizeof x);

  return 0;
}