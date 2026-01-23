#include <stdio.h>
#include <stdlib.h>

/*
      Aula 6
  Lendo números caracteres
*/
int main(void) {

  // tipo nome
  char sexo = 'k'; // precisa colocar em aspas simples

  printf("Valor da variavel sexo: %c\n", sexo);

  printf("Digite seu sexo: (f,F,m ou M)");
  scanf("%c", &sexo);
  printf("Valor da variavel sexo: %c", sexo);

  
  return 0;
}