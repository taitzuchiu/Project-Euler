#include <stdio.h>

int main(){
  int i, total;

  for (i = 1; i < 10000000; i++){
    total += is_chain_89(i);
  }

  printf("Answer: %d \n", total);
  return 0;
}

int is_chain_89(int num){
  int prev = sqsum_digits(num);
  int next;

  while(1){
    next = sqsum_digits(prev);
    if (next == 1){
      return 0;
    }
    else if (next == 145 || next == 42 || next == 20 || next == 4 || next == 16 || next == 37 || next == 58 || next == 89){
      return 1;
    }
    prev = next;
  }
}

int sqsum_digits(int num){
  int sqsum = 0;
  while(num){
    sqsum += (num % 10)*(num % 10);
    num /= 10;
  }
  return sqsum;
}
