#include <stdio.h>
#include <stdlib.h>
#include <time.h>



int dado (void){
    int dado1;
    srand(time(NULL));

    dado1 = 1 + rand()%6;
    printf("O número sorteado é: %d\n", dado1);
    return 0;
}




