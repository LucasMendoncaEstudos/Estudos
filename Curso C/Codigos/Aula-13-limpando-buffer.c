#include <stdio.h>


/*
      Aula 13 
      Ler dois caracteres
*/
int main(void) {

  char a,b;

  printf("Digite duas letras: ");
  scanf("%c %c", &a,&b);

  //buffer do teclado => quando digita algo ele ja capta pode ser qualquer coisa como o ENTER, TAB e o ESPAÇO.

  printf("Primeira letra: %c\nSegunda letra: %c\n", a,b);
  
  
  
  return 0;
}