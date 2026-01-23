#include <stdio.h>
#include <stdlib.h>

char sexo;
int idade;
float peso, altura;



int main(void) {

  printf("Digite seu Sexo(f, F, m, M), Idade, Peso e ALtura (Nesta Ordem): ");
  scanf("%c%d%f%f",&sexo,&idade,&peso, &altura); //pedindo as informações em uma linha apenas.

  printf("Sexo: %c\nIdade: %d\nPeso: %.1f\nAltura: %.2f", sexo, idade, peso, altura);
  return 0;
}