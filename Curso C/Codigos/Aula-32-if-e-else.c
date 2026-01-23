#include <stdio.h>
#include <stdlib.h>

/*       Aula 40: Decisão completa
  Verificando se um número é negativo
*/
int main(void) {
  int a ;
  printf("\n Digite um valor qualquer: ");
  scanf("%d", &a);
  
  printf("Operador ternário:\n");
  a < 0 ? printf("\n\tValor negativo!\n") :
    a > 0 ? printf("\n\tValor positivo!") : printf("\n\tValor igual a zero"); // uma outra opção para ver estruturas condicionadas.

  printf("\n\nIf/esle\n\n");
  if(a < 0){
    printf("\n\tValor negativo!\n");
  }
  else {
    if(a == 0){
    printf("\n\tValor igual a 0"); 
    }
    else
      printf("\n\tValor Positivo!");
  }
  printf("\nContinuação do programa...\n");
  return 0;
}