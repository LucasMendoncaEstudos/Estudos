#include <stdio.h>
/*
1) Escreva um programa em C que leia três valores e apresente qual é o maior e qual é o menor.
2) Escreva um programa em C que lê 5 números inteiros, um por vez. Conte quantos destes valores
são negativos e quantos são positivos. Ao final, imprima na tela a quantidade de números negativos
e positivos.
3) Escreva um programa em C que leia um número e informe se ele é divisível por 2, por 3 ou por
5, ou se não é divisível por nenhum deles.
4) Crie um programa que permita ao usuário escolher entre fazer a conversão de Real para Dólar ou
de Dólar para Real. Utilize como taxa de câmbio $1 igual a R$5.30.
5) O IMC (Índice de Massa Corporal), pode ser calculado dividindo-se o peso da pessoa (em kg)
pela altura (h em metros) elevada ao quadrado (IMC= m/h2). Escreva um programa que leia o peso
e a altura de uma pessoa, calcule e mostre o IMC e a faixa em que o indivíduo se enquadra de cordo
com a tabela abaixo:

IMC Interpretação
Menor que 18,5 Abaixo do peso
Entre 18,5 e menor que 25 Peso normal
Entre 25 e menor que 30 Sobrepeso
Entre 30 e menor que 35 Obesidade grau 1
Entre 35 e menor que 40 Obesidade grau 2
Maior ou igual a 40 Obesidade grau 3
6) Faça um programa para ler um número inteiro e verificar se corresponde a um mês válido no
calendário. Caso corresponda, escrever o nome do mês, caso contrário, escrever a mensagem ‘Mês
Inválido’.
7) Faça um programa que peça ao usuário um caracter e diga se é uma vogal ou não.
8) Elabore um programa que, dado o número do mês, indica quantos dias têm esse mês. Utilize para
isso a estrutura de seleção switch.
Obs.: Considere fevereiro como tendo 28 dias.
9) Um usuário deseja um programa onde possa escolher que tipo de média deseja calcular a partir
de três notas. Faça um programa que leia as notas e o tipo da média escolhida pelo usuário e calcule
a apresente a média:
Opções:
• ‘a’ - Aritmética.
• ‘p’ - Ponderada (pesos: 3,3,4).
10) Faça um programa que, dado três valores a, b e c, verifique se eles podem ser os comprimentos
dos lados de um triângulo. Caso positivo, seu programa deve informar também se o triângulo é
equilátero, isósceles ou escaleno. Caso contrário, seu programa deve escrever a mensagem “Não
formam um triângulo”.
*/


int main(void) {

  int a,b,c,d,e;
  int negativo = 0, positivo = 0;
  printf("Digite o 1° número: ");
  scanf("%d", &a);
  printf("Digite o 2° número: ");
  scanf("%d", &b);
  printf("Digite o 3° número: ");
  scanf("%d", &c);
  printf("Digite o 4° número: ");
  scanf("%d", &d);
  printf("Digite o 5° número: ");
  scanf("%d", &e);
  if(a < 0){
    negativo ++;
  }else{
    positivo ++;
  }
  if(b < 0){
    negativo ++;
  }else{
    positivo ++;
  }
  if(c < 0){
    negativo ++;
  }else{
    positivo ++;
  }
  if(d < 0){
    negativo ++;
  }else{
    positivo ++;
  }
  if(e< 0){
    negativo ++;
  }else{
    positivo ++;
  }
  printf("São %d positivos e %d negativos",positivo, negativo);









  
  /*
  1)
  int a, b, c ,menor, maior;
  printf("Digite 3 valores:");
  scanf("%d %d %d", &a,&b,&c);

  if(a<b){
    if(a<c){
      menor = a;
    }
    else{
      menor = c;
    }
  }
  else{
    if(b < c){
      menor = b;
    }
    else{
      menor = c;
    }
  }
  if(a > b){
    if(a > c){
      maior = a;
    }
  else{
    maior = c;
  }
  }
  else{
    if(b>c){
      maior = b;
    }
    else{
      maior = c;
    }
  }
  printf("\n\tMaior: %d\n\tMenor: %d",maior,menor);
  */
  
  return 0;
}
