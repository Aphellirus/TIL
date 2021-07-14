#include <iostream>
using namespace std;

int main() {
    int a;
    cin>>a;
    int c=a*10;
    for(int b=a; b<=c;b+=a){
        cout<< b<<endl;
    }
    return 0;
}
