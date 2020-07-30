#include<time.h>
#include<stdio.h>
#include<stdlib.h>

int main(){
   srand((unsigned)time(NULL));
   printf("%p",rand());
   return 0;
}
