#include <iostream>
using namespace std;

int main() {
int x,i,b=0;
cin >> x;
if (x==0)
cout <<"square root of ("<< x << ") = "<< x;
else{
for (i=1;i<=x;i++)
    if (x % i == 0)
      if (i * i == x){
        cout <<"square root of("<< x << ") = "<< i;
        b =1;
        break ;}
  if (b == 0)            
 cout << "No square root of "<< x;
}
}
