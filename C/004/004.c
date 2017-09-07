#include <stdio.h>
#include <math.h>
#include <string.h>

int main(){
  int largest = 0;
  int i, j;

  for (i = 999; i > 0; i--){
    for (j = 999; j > 0; j--){
      int prod = i * j;
      char str[12];
      sprintf(str, "%d", prod); //convert prod into string

      if (is_palindrome(str) & prod > largest ) {
        largest = prod;
      }
    }
  }

  printf("Answer: %d \n", largest);
  return 0;
}

int is_palindrome(char str[]){
  int i, j;
  int length = strlen(str)-1;

  for (i = 0; i <= floor(length); i++){
    j = length - i;
    if (str[i] != str[j]){
      return 0;
    }
  }

  return 1;
}
