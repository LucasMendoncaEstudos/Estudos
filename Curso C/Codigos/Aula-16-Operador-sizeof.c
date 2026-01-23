#include <stdio.h>


/*
        Aula 16
        operador sizeof
        sizeof x ou sizeof(int)

*/
int main(void) {

  float x = 1.0;
  
  printf("Tamanho de um float na memoria: %d bytes\n", sizeof x);
  printf("Tamanho em memoria de um int: %d bytes \n", sizeof(int));
    
  
  return 0;
}