#include <stdio.h>
#include <math.h>

long int p_n(int n, long int p[101], int m[20], int s[20]){
  long int pn = 0;
  int i = 1;
  while (m[i] <= n){
    pn += s[i] * p[n - m[i]];
    i+=1;
  }

  return pn;
}

int main(){
  int m[20]; // pentagonal numbers
  int s[20]; // corresponding pentagonal signs

  m[0] = 0;
  fill_m(m);

  s[0] = 1;
  fill_signs(s);

  long int p[101];
  p[0] = 1;
  p[1] = 1;
  p[2] = 2;

  for (int i = 3; i < 101; i++){
    p[i] = p_n(i, p, m, s);
  }
  printf("Answer: %d\n", p[100]-1);
  return 0;
}

//Generate pentagonal numbers
void fill_m(int m[20]){
  int i, j;
  j = 1;
  for (i = 1; i < 20; i += 2){
    m[i] = (j * (3*j - 1))/2;
    m[i+1] = (-j * (3*-j - 1))/2;
    j += 1;
  }
}

//Generate appropriate signs
void fill_signs(int s[20]){
  int sign = 1;
  for (int i = 1; i < 20; i += 2){
    s[i] = sign;
    s[i+1] = sign;
    sign *= -1;
  }
}
