import java.util.Scanner;
public class Reverse_the_no
{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int r = 0;
        System.out.println("Number = " + n);
        while(n!=0){
            r *= 10;
            r += n%10;
            n /= 10;
        }
        System.out.println("Reverse of number = " + r);
    }
}rever
