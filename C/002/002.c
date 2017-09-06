#include <stdio.h>
int main(){
  int limit = 4000000;
  int bef = 1; int prev = 2; int next = 3; int sum = 2;

  while (next < limit) {
    next = prev + bef;
    if (next % 2 == 0){
      sum += next;
    }
    bef = prev;
    prev = next;
  }
  printf("Answer: %d", sum);
  return 0;
}
