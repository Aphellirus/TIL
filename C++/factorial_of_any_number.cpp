/* 
Factorial of a number 'n' is defined as the product of that number with every whole number bellow it. 
For example, the factorial of 4 is 4×3×2×1, which is equal to 24. It is represented using the symbol '!' So, 24 is the value of 4! 
*/



//####
//input method: enter the number you want to calculate
//####

#include <iostream>
using namespace std;

int main()
{
    int num;
    int factorial = 1; //you can change the 'int' to 'long' or 'long long' to calculate bigger factorials.
    cin >> num;
    
    //for positive values & zero 
    if (num >= 0)
    {
        for(int next = 2; next <= num; next++)
        {
        factorial *= next;
        }
    }
    else //for negative values.. See the end notes. 
    {
    factorial = -1; // change the main value 
        for(int next = -2; next >= num; next--){
        factorial *= next;
    }
    }
    
    cout << "The factorial of " << num << " is: " << factorial << endl;
}

/*
There are different types of negative factorials, by default it should return 1 for all negative factorials. However, this is Roman Factorial which can calculate as it is explained in this link: 
http://mathworld.wolfram.com/RomanFactorial.html
*/
