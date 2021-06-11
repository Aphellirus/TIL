#include <stdio.h>
#include <math.h>
#include <stdlib.h>

int integer_Break(int n) {
            if (n == 2) {
                return 1;
            }
             else if (n == 3) {
                return 2;
            } 
            else if (n % 3 == 0) {
                return (int) pow(3, n / 3);
            }
             else if (n % 3 == 1) {
                return 2 * 2 * (int) pow(3, (n - 4) / 3);
            }
             else {
                return 2 * (int) pow(3, n / 3);
            }
        }

int main(void){
    int n ;
    printf ("enter a number:");
    scanf("%d",&n);
    printf("\nMaximum product of %d after breaking the integer %d is: ", n, integer_Break(n));
	return 0;
}
