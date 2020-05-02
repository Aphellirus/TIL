#include <iostream>
using namespace std;

int main() 
{
    int machine =67;
    int num;
    cout<<"Guess the number: ";
    cin>>num;
    
    for(int i=5; i>=1; i--)
    {
        if(num<machine)
        {
            cout<<"The number you have to guess is higher. Try again ";
        }
        if (num>machine)
        {
            cout<<"The number you have to guess is lower. Try again ";
        }
        if(num != machine)
           {
            cout<<"you have " <<i << " tries" <<endl;
            cin>>num;
        }
    }
    if(num == machine)
           {
            cout<<"You win.";
        }
    else // (num!=machine)
    {
        cout<<"You lose.";
    }
    return 0;
}
