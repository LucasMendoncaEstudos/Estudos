#include <stdio.h>
#include <stdlib.h>
/*
2) Elabore um algoritmo que receba, por meio do teclado, dois valores, um para a variável “a” e um para a variável “b”. Em seguida, faça os passos que julgar necessário para que ao final, a variável “a” possua o valor que inicialmente estava em “b” e a variável “b” possua o valor que inicialmente
estava em “a”. Traduza seu algoritmo para a linguagem C e exiba os valores na tela.

3) Faça um programa em C para trocar o valor de duas variáveis inteiras sem utilizar nenhuma variável auxiliar

4) Escreva um programa que leia um valor de despesa de restaurante, o valor da gorjeta (em porcentagem) e o número de pessoas para dividir a conta. Imprima o valor qe cada um deve pagar. Assuma que a conta será dividida igualmente.

5) Uma empresa contrata um encanador a R$ 45,00 por dia. Faça um programa que solocite o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo que são descontados 8% para imposto de renda.

6) Crie um programa em C que permita fazer a conversão cambial entre Regais e Dóladres. Considere como taxa de cambio U$ 1,0 = R$5,30. Leia um valor em Reais e mostre correspondente em Dólares.

7) Faça um programa para ler do teclado uma quantidade de segundos e imprimir na tela a conversão para horas,minutos e segundos ex: 3672 Saida: 1:1:12
*/



int main(void) {

int horas, minutos,segundos, resto;

  printf("Digite um número de segundos para ser convertido: ");
  scanf("%d",&segundos);
  horas = segundos / 3600;
  resto = segundos %3600;
  minutos = resto/60;
  segundos = resto%60;
  printf("%d:%d:%d", horas, minutos, segundos);









/*
  6)
  float reais, dolares;

  printf("Digite quantos reais você quer converter para dolar: ");
  scanf("%f", &reais);
   dolares = reais / 5.30;
  printf("R$ %.2f são U$%.2f.\n", reais, dolares);

5)
  float diaria, dia, aux, valorFinal;
  
  printf("Quantos dias o encanador irá trabalhar: ");
  scanf("%f", &dia);

  
  aux = 45*dia;
  diaria = aux * 8/100;
  valorFinal = aux - diaria;
  printf("Irá receber: R$%.2f\n Desconto R$%.2f\n",valorFinal, diaria);
  
  4)
  // criação das variáveis necessárias
    int numPessoas;
    float valorDespesa, gorjeta, valorTotal, valorPorPessoa;

    // leitura dos dados
    printf("Digite o valor da conta, da gorjeta e a quantidade de pessoas: ");
    scanf("%f%f%d", &valorDespesa, &gorjeta, &numPessoas);

    // cálculos necessários
    valorTotal = valorDespesa * gorjeta/100 + valorDespesa;
    valorPorPessoa = valorTotal / numPessoas;
    printf("Cada um ira pagar R$%.2f\n", valorPorPessoa);

   3) int a,b;
  printf("Digite dois valores: ");
  scanf("%d %d", &a, &b);
  printf("A = %d\t e B= %d\n", a,b);

  a = b + a;
  b = a - b;
  a = a - b;
  
  printf("A = %d e B = %d", a,b);

  2) int a, b , c ;

   printf("Digite dois valores: ");
   scanf("%d %d", &a, &b);
   printf("A = %d\t e B= %d\n", a,b);

   c = a;
   a = b;
   b = c;
   printf("A = %d e B = %d", a,b); */
  return 0;
}