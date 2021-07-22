using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//arrange words in dictionary order
namespace Sorting
{
using Sorting;

    class Program
    {
        static void Main(string[] args)
        {
        string[] str = { "e","d","c","b","a"};
        foreach(string e in str)
        Console.Write(" "+e);
        
      string[] str2 = Arrange.InAscending(str);
      
       Console.WriteLine();
         
         foreach(string e in str)
         Console.Write(" "+e);
        
    
       
        
        }
    }
    
}
namespace Sorting
{
    public static class Arrange
    {
     public static string[] InAscending(string[] arr)
     { 
       string temp;
       string[] tempArr = arr;
       for(int i = 0;i<tempArr.Length-1;i++)
       for(int j = i+1;j<tempArr.Length;j++)
          if(tempArr[i][0]>tempArr[j][0]){
           temp = tempArr[j];
           tempArr [j] = tempArr[i];
           tempArr[i] = temp;}
         
        
       
        return tempArr;
     }
     
     
     public static string[] InDescending(string[] arr)
     {
      string temp;
      string[] tempArr = arr;
      for(int i = 0;i<tempArr.Length-1;i++)
      for(int j = i+1;j<tempArr.Length;j++)
         if(tempArr[i][0]<tempArr[j][0]){
           temp = tempArr[j];
           tempArr[j] = tempArr[i];
           tempArr[i] = temp;
         }
          
     
      return tempArr;
     }
    }

}

