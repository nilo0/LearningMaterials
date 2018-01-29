#include <stdio.h>
#include "./../include/qe.h"


int main()
{
  float a, b, c, x1[2], x2[2];

  printf("Insert Coeffs, space seperated: ");
  scanf("%f %f %f", &a, &b, &c);

  qe_roots(a, b, c, x1, x2);

  printf("x1 = %f + i %f\n", x1[0], x1[1]);
  printf("x2 = %f + i %f\n", x2[0], x2[1]);

  return 0;
}
