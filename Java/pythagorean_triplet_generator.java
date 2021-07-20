//pythagorean triplet generator 
import java.util.*;
public class Program
{
	public static void main(String[] args) {
	Scanner in = new Scanner(System.in);
	System.out.println("Enter value of m ");
	int m = in.nextInt();
	int i = 2*m;
	int j = (m*m)-1;
	int k = (m*m)+1;
	System.out.println("pythagorean triplet: " + i +","+ j +" ,"+ k);
	
		
	}
}
