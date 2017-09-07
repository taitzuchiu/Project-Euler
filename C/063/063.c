#include <stdio.h>
#include <math.h>

int main(){
  int ndpows = 0;
  for (int i = 1; i < 10; i++){
    ndpows += total_nth_powers(i);
  }
  printf("Answer: %d", ndpows);
  return 0;
}

int total_nth_powers(int base){
  int total = 1;
  int req_digits = 2;
  float next = base;

  while(1){
    next = next * base;
    if (next > pow(10,req_digits - 1) && next < pow(10, req_digits)){
      total += 1;
    }
    else {
      return total;
    }
    req_digits += 1;
  }
}
