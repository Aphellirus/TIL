// C program to check if a given
// year is leap year or not
#include <stdio.h>
#include <stdbool.h>
 
bool checkYear(int year)
{
    // If a year is multiple of 400,
    // then it is a leap year
    if (year % 400 == 0)
        return true;
 
    // Else If a year is multiple of 100,
    // then it is not a leap year
    if (year % 100 == 0)
        return false;
 
    // Else If a year is multiple of 4,
    // then it is a leap year
    if (year % 4 == 0)
        return true;
    return false;
}
 
// driver code
int main()
{
    int year = 2000;
 
    checkYear(year)? printf("Leap Year"):
                   printf("Not a Leap Year");
    return 0;
}