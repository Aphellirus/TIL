#include <iostream> // cout endl 
using namespace std;
#include <vector> //vector 
#include <cstdlib> //srand rand
#include <ctime> //time

/*
The tables are dynamic and new values can be added.
*/

string ingfix(string);
string locfix(string);
string cap(string);
string anfix(string);

int main() {
    srand(time(0));
    
 vector<string> numbers =
    {" one"," two"," three",
    " four"," five"," six",
    " seven"," eight"," nine",
    " ten"," twenty"," thirty"};
        
 vector<string> Fnames =
    {" Sonia"," Tammy"," Sue",
    " Jill"," Liz"," Anne",
    " Beth"," Kate"," Cathy",
    " Mary"," Patty"," Dora",
    " Minnie"," Daisy"," Sue"};
 
 vector<string> Mnames =
    {" Alex"," Noah"," Dexter",
    " Mike"," Bob"," Jack",
    " Ben"," Matt"," Simon",
    " Carl"," Tony"," Jeff",
    " Phil"," Peter"," John"};
        
 vector<string> relations =
    {" mom"," son"," brother",
    " dad"," boss"," co-worker"};
        
 vector<string> adjective =
    {" good"," new"," first",
    " last"," long"," great",
    " little"," lumpy"," other",
    " old"," right"," big"," high",
    " different"," small"," large",
    " next"," early"," young",
    " important"," few"," public",
    " bad"," same"," able"," soft",
    " ugly"," messy"," happy",
    " extra"};
     
 vector<string> adverbs =
    {" up"," so"," out"," just",
    " now"," how"," then",
    " more"," also"," here",
    " well"," only"," very",
    " even"," wildly"," there",
    " down"," still"," in",
    " as"," too"," when",
    " never"," really"," most",
    " modestly"," stupidly",
    " greedily"," carefully",
    " slowly"," quickly",
    " always"," sometimes"};
    
 vector<string> nouns =
    {" time"," person"," year",
    " way"," day"," thing",
    " man"," world"," life",
    " hand"," part"," child",
    " eye"," woman"," place",
    " work"," week"," case",
    " point"," government",
    " company"," number",
    " group"," problem"," fact",
    " hill"," pail"," water",
    " crown"," trip"," goat",
    " fish"," chicken"," car",
    " hook"," diamond"," bug",
    " mold"," leak"," bait",
    " trip"};
    
 vector<string> verbs =
    {" behave"," do"," say",
    " get"," make"," go"," know",
    " take"," see"," come",
    " think"," look"," want",
    " give"," use"," find",
    " tell"," ask"," work",
    " seem"," feel"," try",
    " leave"," call"," tickle",
    " tumble"," hit"," fight",
    " fish"," hunt"," run",
    " kiss"," hug"," tease",
    " clean"};
    
 vector<string> places=
    {" Italy"," bathroom",
    " store"," outside",
    " school"," library",
    " Mexico"," France",
    " Rome"," Cuba"," Iraq",
    " bedroom"," frontroom",
    " club"," bar"," kitchen"};
      
 vector<string> colors =
    {" red"," green"," blue",
    " yellow"," white"," orange",
    " purple"," brown"," black"};
    
    #define num numbers[rand()%numbers.size()]
    #define Fname Fnames[rand()%Fnames.size()]
    #define Mname Mnames[rand()%Mnames.size()]
    #define name ((rand()%2)>1?Fname:Mname)
    #define relation relations[rand()%relations.size()]
    #define adj adjective[rand()%adjective.size()]
    #define adv adverbs[rand()%adverbs.size()]
    #define noun nouns[rand()%nouns.size()]
    #define verb verbs[rand()%verbs.size()]
    #define place places[rand()%places.size()]
    #define color colors[rand()%colors.size()]
    
    #define ing ingfix(verb)
    
    for(int n(10);n<10;n++)
    cout<<num<<name<<relation
        <<adj<<adv<<endl;
    string x = name;
  
 string str;
 switch (rand()%7){
 case(0):{string n1=noun;
     str = Mname+" and"+Fname+
  " got married and had"
  +anfix(n1)+" named"+name+
  ". It was"+anfix(adj)+n1+" with"+
  color+" eyes.";
      break;
      }
  case(1):{
      string n1(Mname);
      string n2(Fname);
      str = n1+" and"+n2+
      " went up the"+noun+
      " to"+verb+" a pail of"+
      noun+"."+n1+
      " fell down and broke his"+
      noun+" and"+n2+" came"+
      ing+" after.";
      break;
      }
  case(2):{
      string p1= locfix(place);
      str = " I am going on"+
      anfix(noun)+" to"+p1+
      ". I am"+adv+
      " excited! I have planned"+
      anfix(adj)+
      " trip and packed"+
      anfix(noun)+" just in case."+
      cap(p1)+" will be fun.";
      break;
      }
  case(3):{ string s1= noun ;
      str = cap(s1)+
      " porridge hot,"+s1+
      " porridge cold."+cap(s1)+
      " porridge in the"+noun+
      num+" days old.";
      break;
      }
  case(4):{ string n1= name;
      str = " My"+relation+n1+
      " is"+anfix(adj)+" person."+
      n1+" always makes time to"+
      verb+" and go"+ing+".";
      break;
      }
  case(5):{
      str = "While"+ing+
      " out your"+noun+
      ", you should"+adv+
      " check for"+noun+
      " and"+noun+"s. Call a"+
      noun+" if you find any.";
      break;
      }
  case(6):{ string v1(verb);
      str = " I like to"+v1+
      ". while"+ingfix(v1)+
      " I"+adj+" bring plenty of"+
      noun+" and extra"+noun+
      ", in case my"+relation+
      " comes along.";
      break;
      }
  default:{cout<<"loveIt = likeIt;";}
  }
  cout<<endl<<str<<endl<<endl;
    return 0;
}

//present verb fix
string ingfix(string str){
   char tmp=str[str.size()-1];
   if (tmp=='e'){
       if (str[str.size()-2]!='e')
           str.erase(str.end()-1);
   }else 
       if(tmp=='t')
         if (str[str.size()-2]!='h')
           if(str[str.size()-2]!='n')
               str = str + "t";                 
   str=str+"ing";
   return str; 
}

//proper case fix
string cap(string str){
    char tmp = str[1];
    if (tmp>90)
       str[1]=tmp-=32;
     return str;  
}

// location grammar fix
string locfix(string str){
    char tmp = str[1];
    if (tmp>90){
       str = " the"+str;
   } 
   return str;
}

// first letter vowel fix
string anfix(string str){
    char tmp = str[1];
    if (tmp=='a'||tmp=='e'||tmp=='i'||tmp=='o'||tmp=='u')
       str = " an"+str;
    else
       str = " a"+str;
    return str;
}
