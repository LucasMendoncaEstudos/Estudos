#include <stdio.h>
#include <stdlib.h>


int main(){

    int x,y;
    long long int z;

    printf("Digite 3 números:");
    scanf("%d %d %lld",&x,&y,&z);

    printf("Os números que voce digitou foram: %d, %d e %lld\n", x,y,z);
    printf("O tamanho do primeiro é de %d\n Do segundo é %d\n Do terceiro é %d",sizeof x,sizeof y, sizeof z);


    return 0;
}