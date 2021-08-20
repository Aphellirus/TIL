import java.util.Scanner;
import java.lang.Math;

public class Main {
    
    public static void main(String[] args) {
		
        double a;
        double b;
        double c;

        Scanner scanner = new Scanner(System.in);


        System.out.println("Enter side a: ");
        a = scanner.nextDouble();
        System.out.println("Enter side b: ");
        b = scanner.nextDouble();


        c = Math.sqrt((a*a)+(b*b));

        System.out.println("The hypotenuse is : "+Math.round(c));

        scanner.close();
	}
}
