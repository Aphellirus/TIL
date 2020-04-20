include <iostream>
using namespace std;



void triforce(const int & n){
    cout<<endl<<string(35,'-')<<"\nInput: "<<n;
    for(int r=1, spacing=n;r<=n;++r){
        cout<<endl<<string(n+--spacing,' ');
        for(int i=0;i<r;++i) cout<<"* ";
    }
    for(int r=1, spacing=n;r<=n;++r){
        cout<<endl<<string(--spacing,' ');
        for(int i=0;i<r;++i) cout<<"* ";
        cout<<string(2*spacing,' ');
        for(int i=0;i<r;++i) cout<<"* ";
    }
}



int main() {
    for(int n=1;n<10;++n) triforce(n);
    return 0;
}
