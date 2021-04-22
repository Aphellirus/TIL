import java.util.*;
import java.io.*;

class Function
{
  
  static final int[] INTEGERS = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
  
  static final String[] ROMANS = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};

 
public String intToRoman(int num) {
  for (int i = 0; i < INTEGERS.length; i++) {
    if (num >= INTEGERS[i]) {
      return ROMANS[i] + intToRoman(num - INTEGERS[i]);
    }
  }
  return "";
    }
}
    
    
  public class Program{
  
  public static void main(String[] args){
     PrintWriter p = new PrintWriter(System.out, true);
     
         Scanner input = new Scanner(System.in);
    int num = input.nextInt();
     
     Function f = new Function();
     
     
     p.println(num + " in Roman numerals = " + f.intToRoman(num) );
  }
}
