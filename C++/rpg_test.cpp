#include <iostream>
using namespace std;

int main()
{
    cout<<"You have been captured by a wIzard, the only way to escape Is by stealing his wand."<<endl<<"The Wand is placed secure in a magic coffer, which you will need to unlock."<<endl<<endl;
    int code, lock=0,Q1;
    cout<<"The coffer is in front of you"<<endl<<endl;
    cout<<"Do you want to attempt to steal the wand? you only have time to attempt the code three times in order to unlock the coffer,"<<endl<<"to proceed type '448'"<<endl;
    cin>>Q1; if (Q1!=448)
                {
                    cout<<"so you don't wanna try?"<<endl;
                    cout<<"\nHowever, you curiously try to put the code once as you are scared to do not."<<endl<<endl;
                    lock+=2;
                }
    do {
        cout<<"what sIngle dIgIt you tell shall raIse the wand?"<<endl;
        cin>>code;if(code==1){
                    lock=3;
                    cout<<"You got the wand and now you waved it and killed the wIzard somehow. Now you are free of the trouble but you will never get away with this trauma of killing somebody."<<endl
                    <<"Now you live the life of a wIzard and kidnaps children to immolate 'em as the wand requires it to keep it's possessor alive, thats you.";
                    }
                    else lock++;

    }while(lock!=3);
    if (code!=1)cout<<"wIzard: mmmhahahhaha youi tri to steail wand, NOI WAYI!!"<<endl<<endl<<"wIzards kills you and feeds on your every organ";
    cout<<"\n\n\n     The End\n\n\n";

    system ("pause");
    return 0;
}
