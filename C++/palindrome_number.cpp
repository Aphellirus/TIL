/*Enter a number.*/
#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;
int main() {
    string s;
    cin>>s;
    const string n = s;
    reverse(s.begin(), s.end());
    if (n == s)
    {
        cout<<n<<" is a palindrome number.";
        return true;
    }
    else {
        cout<<n<<" isn't a palindrome number.";
        return false;
    }
    return 0;
}
