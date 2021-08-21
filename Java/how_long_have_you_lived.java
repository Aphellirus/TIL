import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int age = scanner.nextInt();

int months = age * 12;
int weeks = age * 52;        
int days = age * 365;
int hours = days * 24;
int minutes = hours * 60;
int seconds = minutes * 60;

System.out.println("You have lived for...");

System.out.println(months+ "  months");

System.out.println(weeks+ "  weeks");

System.out.println(days+ "  days");

System.out.println(hours+ "  hours");

System.out.println(minutes+ "  minutes");

System.out.println("and for... " +seconds+ "  seconds");

   }
}
