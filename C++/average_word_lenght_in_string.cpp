#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
using namespace std;

int main()
 {

string str;
getline(cin,str);


int count_spaces = count(str.begin(), str.end(), ' ');

int count_words = ++count_spaces;


auto p = remove(str.begin(), str.end(), ' ');

int size_str=0;

for(auto it=str.begin(); it!=p; it++)
{
if((static_cast<int>(*it)>=65 && static_cast<int>(*it)<=90) ||(static_cast<int>(*it)>=97 && static_cast<int>(*it)<=122))
    
    {
  size_str++;
  }
  cout<<*it;
}

cout<<endl<<"Count words: "<<count_words<<endl;
cout<<"Count letters: "<<size_str<<endl;


double aver_words_len=ceil(static_cast<double>(size_str)/count_words);

cout<<"Average word length: "<< aver_words_len<<endl;


    return 0;
}
