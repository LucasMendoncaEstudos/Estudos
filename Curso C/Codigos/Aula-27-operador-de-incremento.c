#include <stdio.h>

/*
      Aula 27
    Operador de incremento ++ e decremento --

*/
int main(void) {
  int resultado,contador = 10;
  // sinônimas
  // contador++;
  // contador += 1;
  // contador = contador + 1;

  resultado = --contador;
  printf("Valor: %d\n", resultado); // precisa colocar o operador a esquerda da variavel

  
  return 0;
}