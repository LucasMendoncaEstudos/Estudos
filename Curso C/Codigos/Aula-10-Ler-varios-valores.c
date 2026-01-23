#include <stdio.h>
#include <stdlib.h>

/*
        Aula 10
    Lendo vários valores

*/
int main(void) {

  int num1;
  int num2;
  int num3;

  printf("Digite 3 números inteiros: ");
  scanf("%d%d%d",&num1, &num2, &num3);

  printf("Os numeros digitados foram: %d, %d, %d\n", num1, num2, num3);

  
  return 0;
}