#include <stdio.h>

int encontrarDivisoresComuns(int a, int b, int lista[]) {
    int menor = (a < b) ? a : b;
    int count = 0;

    for (int i = 1; i <= menor; i++) {
        if (a % i == 0 && b % i == 0) {
            lista[count] = i;
            count++;
        }
    }

    return count; // Retorna o total de divisores comuns encontrados
}

int main() {
    int num1 = 48, num2 = 18;
    int divisores[100]; // Vetor para armazenar os divisores comuns
    int total = encontrarDivisoresComuns(num1, num2, divisores);

    printf("Divisores comuns entre %d e %d:\n", num1, num2);
    for (int i = 0; i < total; i++) {
        printf("%d ", divisores[i]);
    }
    printf("\n");

    return 0;
}



#include <stdio.h>

// Função que retorna o MDC de dois números
int mdc(int a, int b) {
    while (b != 0) {
        int resto = a % b;
        a = b;
        b = resto;
    }
    return a;
}

int main() {
    int num1 = 48, num2 = 18;
    printf("O MDC de %d e %d é: %d\n", num1, num2, mdc(num1, num2));
    return 0;
}
