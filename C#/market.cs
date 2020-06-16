using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

 namespace Market
 {
   public class Products
   {
     public string Code ,Prod;
     public int quan;
     public double price,total;
     public double finalPrice,addPrice;
     
     public void Menu()
     {
       Console.WriteLine("Product   Code   Price");
       Console.WriteLine("Apple      1      ¥25");
       Console.WriteLine("Papaya     2      ¥30");
       Console.WriteLine("Orange     3      ¥10");
       Console.WriteLine("PineApple  4      ¥40");
       Console.WriteLine("Avocado    5      ¥27\n");
     }
     public void choose()
     {
       Console.Write("Enter Product Code(1-5): ");
       this.Code = Convert.ToString(Console.ReadLine());
       
       if (Code == "1")
         Prod = "Apple(¥25)";
       else if (Code == "2")
         Prod = "Papaya(¥30)";
       else if (Code == "3")
         Prod = "Orange(¥10)";
       else if (Code == "4")
         Prod = "Pineapple(¥40)";
       else if (Code == "5")
         Prod = "Avocado(¥27)";
       else
         Prod = "Not Available";
       Console.WriteLine("Product: {0}",Prod);
      }
      
      public double GetPrice()
      {
        if (Code == "1")
         price = 25;
       else if (Code == "2")
         price = 30;
       else if (Code == "3")
         price = 10;
       else if (Code == "4")
         price = 40;
       else if (Code == "5")
         price = 27;
       else
         price = 0;  
       return price;
      }
      
      public void Compute()
      {
        if (Code != "1" && Code != "2" && Code != "3" && Code != "4" && Code != "5")
          quan = 0;
        else
        {
          Console.Write("Enter Quantity: "); 
          quan = int.Parse(Console.ReadLine());
        }
        total = quan*price;
        Console.WriteLine("Amount: ¥{0}\n",total);
      }  
   
     public class Program
      {
        public static void Main(string[] args)
         { 
             int a = 0; 
             int YesNo;     
             
             Console.WriteLine("Welcome to our Market\n");
             Products p1 = new Products();
             p1.Menu();
             
             p1.choose();
             p1.GetPrice();
             p1.Compute();
             p1.addPrice += p1.total;
             Console.WriteLine("Total Price: ¥{0}\n",p1.addPrice);
             
             for(int i = 0; i==a ; i++)
             {
               
               Console.Write("Order Again? YES(1) NO(2): ");
               YesNo = int.Parse(Console.ReadLine());
               if(YesNo == 1)
               {
                  p1.choose();  
                  p1.GetPrice(); 
                  p1.Compute(); 
                  p1.addPrice += p1.total;
                  a++;
               }
               else
                  break;
               Console.WriteLine("Total Price: ¥{0}\n",p1.addPrice);
             }     
            
             Console.WriteLine("Thank You for your purchased!\n    TOTAL AMOUNT: ¥{0}",p1.addPrice);
         }
      }
    }
 }
