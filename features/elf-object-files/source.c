#include <stdio.h>
#include <math.h>
#include <stdlib.h>
// Compiled with -fno-stack-protector, so we don't have useless readquadword calls

// Declare the function prototype, and use it
int extern_int(int a, int b);

const char* sfoo = "foo";

// This functions is here because sometimes symbol _GLOBAL_OFFSET_TABLE_
// is incorrectly used as name of this function, so this function is not
// tested.
void asd(void) {
  printf("Random num: %d\n", rand());
}

int func_int(int a, int b) {
  puts(sfoo);
  return a + b;
}

double func_double(double a, double b) {
  puts(sfoo);
  return a + sqrt(b);
}

float func_float(float a, float b) {
  puts(sfoo);
  return a + b;
}

int main(void) {
  asd();
  printf("Hello, world!");
  printf("%d\n", func_int(5, 10));
  printf("%d\n", extern_int(5, 10));
  printf("%g\n", func_double(3.14, 123.321));
  printf("%g\n", func_float(3.14f, 123.321f));
  return 0;
}
