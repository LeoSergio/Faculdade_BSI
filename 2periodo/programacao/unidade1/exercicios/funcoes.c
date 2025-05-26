#include <stdio.h>


int fat(int n)
{
 int i, f;

 f = 1;
 for (i = 1; i <= n; i++)
 f *= i;
 return f;
}
/* Implementação da função Arranjo */
/* Calcula o arranjo de n valores tomados k a k
*/
int arr(int n, int k)
{
 return (fat(n) / fat(n - k));
}
/* Implementação da função Combinação */
/* Calcula a combinação de n valores tomados k
a k */
int comb(int n, int k)
{
 return (fat(n) / ((fat(k) * fat(n - k))));
}
