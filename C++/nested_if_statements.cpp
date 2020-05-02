#include <iostream>
using namespace std;

int main()
{
    int score;
    cin >> score;
    if (score >= 70) {
        if(score >= 100) {
            cout <<"You got a perfect score!";}
        else {
            cout << "You passed!";}
    }
    else {
        if (score > 0) {
            cout << "Good try! Better lucl next time!";
        }
        else {
            cout << "-Invalid-";}
    }
    return 0;
    }
