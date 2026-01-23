#include <stdio.h>


/*
      Aula 18
      tamanho de um int na memória
      intervalo: -2.147.483.648 a 2.147.483.648
      Aula 19
      operador long para o tipo int
      %li / %ld
*/

int main(void) {

  long long int x = 2147483648;

  printf("O valor de x em bytes : %d\n", sizeof x);
  printf("O valor de x : %lld\n", x);
  x++;
  printf("O valor de x : %lli\n", x);
  return 0;
}