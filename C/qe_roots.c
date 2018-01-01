#include <math.h>
#include "./delta.h"

void qe_roots(float a, float b, float c, float x1[2], float x2[2])
{
  float d = delta(a, b, c);
  if(d >= 0)
  {
    x1[0] = (-b + sqrt(d)) / (2 * a);
    x1[1] = 0.0;
    x2[0] = (-b - sqrt(d)) / (2 * a);
    x2[1] = 0.0;
  }
  else
  {
    x1[0] = -b / (2 * a);
    x1[1] = sqrt(-d) / (2 * a);
    x2[0] = -b / (2 * a);
    x2[1] = -sqrt(-d) / (2 * a);
  }
}
