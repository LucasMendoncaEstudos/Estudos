#include <stdio.h>

// caractere de escape para saltar uma linha -> \n
int main(void) {
  // printf("") é uma função de saida
  printf("\nOlá \nseja \nbem \nVindo!\n");
  printf("\n ########");

  printf("\n------------------------------------------\n");
  printf("1- Logar    2- Cadastrar   3- Imprimir");
  printf("\n------------------------------------------\n");

  printf("\n Valor retornado: %d", printf("Bom")); //ele vai imprimir 3, pq são o número de caractéres

printf("\nPressione qualquer tecla para finalizar.");
getchar(); // recomendado utilizar isso para não utilizar o system("pause"); pois ele da alguns erros no sistema.

  return 0;
}