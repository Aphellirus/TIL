#include<iostream>
using namespace std;

int main(){

    int a, b, sum = 0;
    cout << "Enter a range of numbers: ";
    cin >> a >> b;
    //cout << "Odd range numbers" << endl;
    do{
        if(a % 2 == 1){
            cout << a << " ";
            sum += a;
        }
        a++;
    }
    while(a >= 0 && a <= b);
    cout << endl << "Sum of odd numbers in the range: " << sum;

    return 0;
}
