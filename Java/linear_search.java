import java.util.Scanner;

 class LinearSearch
 {
   //attributes
   private Scanner scan;
   private int[] arr = {10,20,500,11};
   private int uInput;
   private int key;
   
   public LinearSearch()
   {
     scan = new Scanner(System.in);
     
     linearSearch(arr); 
   }
   
   //methods
   //1. Compare the leftmost arr to the 
   //   uInput(user input)
   public int linearSearch(int[] arr)
   {
     //Search data/element from array
     System.out.print("Search data: ");
     uInput = scan.nextInt();
     
     //1.a Compare the uInput throughout arr
     for( int ctr = 0; ctr < arr.length; ++ctr )
     {
       if( uInput == arr[ctr] )
       {
         System.out.println( "Data Found on Element: " + ctr );
         key = 1; //1 means found!
         break;
       }
       else
       {
         key = 0; //0 means not found!
       }
       
     }
     
     if(key == 0)//if data  not found display this..
     {
         System.out.println( "Search Not Found!: " + (-1) );
     }
     
     return uInput;
   }
   
 }
 
 public class dcderLa_p2_LinearSearch
 {
   public static void main(String [] args)
   {
     new LinearSearch();
   }
 }
