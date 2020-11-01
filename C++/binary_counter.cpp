#include <iostream>
#include <bitset>

using namespace std;

int main() {
    //declare variables
    bitset <4> binval;

    for (int i =0; i < 16; i++) {
        binval = bitset<4>(i);
        cout << binval << endl;
    }
    
    return 0;
}
