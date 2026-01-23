#include <stdio.h>

/*
        Aula 12
    Ler idade, peso, altura e sexo
*/
int main(void) {
  char sexo;
  int idade;
  float peso, altura;

  printf("Digite sua idade, peso, altura e seu sexo f ou m: ");
  scanf("%d%f%f %c", &idade, &peso, &altura, &sexo); //Colocamos o espaço entre o %f e %c para ele desconsiderar ou o espaço do teclado ou o enter
  printf("Idade: %d\nPeso: %.2f\nAltura: %.2f\nSexo: %c\n", idade, peso, altura, sexo);
  
  return 0;
}