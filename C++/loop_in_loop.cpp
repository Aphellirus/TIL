#include <iostream>
using namespace std;

int main() {
   int j,i,k;
   for(i=0;i<=10;i++){
       for(j=0;j<=10;j++){
           for(k=0;k<=10;k++){
                   cout <<i<<"×"<<j<<"×"<<k<<"="<<i*j*k<<endl;
           }
       }
   }
    return 0;
}
