//To find the number is odd or even
import java.util.Scanner;
public class Helloprogramming{
    public static void main(String[] args){
//to creat the program to import the scanner
        Scanner fn=new Scanner(System.in);
        System.out.println("ENTER ANY NUMBER");
        int num=fn.nextInt();
        int remaninder=num % 2;
//  "%" sign helps to find the remainder
// using (if....else) conditional to find the remainder
        if (remaninder == 0){
            System.out.println(num+" is even");
        }else{
            System.out.println(num+" is odd");
        }
    }
}
