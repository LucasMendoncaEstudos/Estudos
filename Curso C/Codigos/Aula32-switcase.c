#include <stdio.h>

/*
      Aula 50 switch case
    teste: - cadastrar produto
    -vender produto
    -buscar produto
    -imprimir relatório
    -sair

*/

int main(void) {
  int opcao;
  printf("1- Cadastrar produto\n2 - Vender produto\n3 - Buscar prduto\n4 - Imprimir relatório\n5 - sair\n Opção: ");
  scanf("%d", &opcao);

  switch(opcao){
    case 1:
    printf("\nCadastrando novo produto.\n");
    break;
    case 2:
    printf("\nVendendo um novo produto.\n");
    break;
    case 3:
    printf("\n Buscando novo produto...\n");
    break;
    case 4:
    printf("\nImprimindo relatório\n");
    break;
    case 5:
    printf("\nSaindo...\n");
    break;
    default:
    printf("\nOpção invalida!\n");
  }


  
  return 0;
}