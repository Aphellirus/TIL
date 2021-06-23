import java.util.Scanner;

public class DigitSum
{


public static int sumOfDigit(int value){
    
    int sum =0;
    int lastNum = 0;
    
 while (value>0){
     
     lastNum = value%10;
     sum+=lastNum;
     value/=10;
 }  
 
 
 return sum;
    
}




    public static void main(String[] args) {
        
        Scanner input = new Scanner(System.in);
        
        int value = input.nextInt();
        System.out.println("Enter a number to see the sum of all it's digits: " +"'"+value+"'");
        
        int digitSum = sumOfDigit(value);
        
        System.out.println("The Sum of all digits in your number is: "+digitSum);
        
    }
}
