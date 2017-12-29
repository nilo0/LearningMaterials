#include <stdio.h>
#include <math.h>
#include "./delta.hrm"

int main()
{
  float a, b, c, d, x1, x2;
  printf("Insert Coeffs, space seperated: ");
  scanf("%f %f %f", &a, &b, &c);
  d = delta(a, b, c);
  if(d >= 0)
  {
    x1 = (-b - sqrt(d)) / (2 * a);
    x2 = (-b + sqrt(d)) / (2 * a);
    printf("roots = %f, %f\n", x1, x2);
  }
  else
  {
    printf("there is no real root\n");
  }

  return 0;
}
