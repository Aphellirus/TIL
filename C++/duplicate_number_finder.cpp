#include<iostream>
using namespace std;

const int u = 5;
int duplicate ;
int firelock[u] = {3 , 1, 3 , 4 , 5};// You can change the nums in here ....
bool t = false;

class xlock
{
    public :
            void showlock()
            {
                cout << "\nArrays : \n\n";
                for(int i = 0; i < u;i++)
                {
                    cout << firelock[i] << " ";
                }
                cout << "\n\n";
            }
            void beautylock()
            {
                 for(int i = 1; i <= 20;i++)
                 {
                     cout << "__";
                 }
                 cout << "\n\n";
            }

            void keylock()
            {
                 for(int i = 0; i < u;i++)
                 {
                     for (int j = 0; j < u; j++)
                     {
                         if(i == j)
                         {
                             j++;
                             continue;
                         }
                         if(firelock[i] == firelock[j])
                         {
                                t = true;
                                duplicate = firelock[j];
                                //break;
                         }

                        
                     }
                      if(t == true)
                         {
                             break;
                         }
                     
                 }
                 if(t == true)
                 {
                     cout << "\n\nDuplicate number in the array : " << duplicate << "\n\n";
                 }else{
                     cout << "\n\nNo duplicate number found ... \n\n";
                 }
            }
};


int main()
{
    xlock sudolock;
    sudolock.showlock();
    sudolock.beautylock();
    sudolock.keylock();
    return 0;
}
