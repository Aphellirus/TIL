#include <stdio.h>

int sum=0;

int* sumz(int n){
    sum = (n*(n+1))/2;
    return &sum;
}

int main() {
    int *ptr = sumz(5);
    printf("%d\n",*ptr);
    ptr = sumz(10);
    printf("%d\n",*ptr);
    
    return 0;
}
