/*
This Program Check Weather the Input(string) is Prime or Not.

A String is called Prime if it can't be constructed by concatenating multiple (more than one) equal strings.

For example:
    "abac" is prime, 
but "xyxy" is not ("xyxy" = "xy" + "xy").


Examples
Input: "xyxy"
Output: "not prime"

Input: "aaaa"
Output: "not prime"

Input: "hello"
Output: "prime"

*/
#include <iostream>
#include <string>
using namespace std;

bool Prime_String(string str)
{
 int len=str.length();
 string temp[20];
 
 int i,c=0;
 for(i=0;i<len;i++) 
 {
  if(i>0 && str[0]==str[i])
   c++;
  temp[c]+=str[i];
 } 
/*
 for(i=0;i<=c;i++){
  cout<<i <<" -> "<<temp[i]<<endl;
 }
 cout<<endl;
*/ 
 if(!str.compare(temp[0]) || len%2)
   return true;  
    
 int f=1; 
 string sumstr;
 for(i=0;i<c;i++){
   f=f&& !(temp[0].compare(temp[i+1]));
   sumstr += temp[i];
 }
 sumstr+=temp[c];

 return !(!str.compare(str) && f);
}

int main() 
{
  string str;  
//cout<<"Enter a String: ";
  getline(cin,str);
  cout<<"Entered String: "<<str<<endl<<endl;
  
  if(Prime_String(str))
   cout<<"✔️ It's is a Prime String.";
  else
   cout<<"❌ It's Not a Prime String.";
   
  return 0;
}
