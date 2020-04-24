//USER INPUT NEEDED: 1 time

#include <iostream>
using namespace std;

int main()
{
    int limit, valueA=0, valueB=1;
    cout<<"Lets make a Fibonacci numerical series, you decide how long you want the series to be"<<endl
    <<"Enter length number (The higher number you type the higher the series will be): "; cin>>limit;
    
    if (limit==0) cout<<"Error: The series is nothing"<<endl;
    else if (limit>=1)
    {
    cout<<"> "<<valueA<<endl; 
    cout<<"> "<<valueB<<endl;
    }
    /*why these two A & B values? the 1st value in the fibonacci series have to be the sum of previous 2 values technically speaking. Let's say if you want the 1st value in the series which is 1(S1) so,
        S1 = sum of previous 2 value
        0, 1, 1(S1)
        S1 = 0+1 = 1
        
        another example for this, S2=?
        0, 1, 1(S1), 2(S2)
        S2 = 1 + 1 = 2
        
        The actual starting point of the series is from S1
        But just to be clear what is going on (see previous example) i wrote the else if line.
    */

    for (int FiboValue; limit>=1; limit--)
    {
        FiboValue = valueA+valueB;
        cout<<"> "<<FiboValue<<endl;
        valueA = valueB, valueB = FiboValue;
    }

    system ("pause");
    return 0;
}
