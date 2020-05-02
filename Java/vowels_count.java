import java.util.*;

public class Program
{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        String input = scanner.nextLine();
        int vowels = input.replaceAll("[^AaEeIiOoUu]", "").length();
        int length = input.length();
        
        System.out.println("Input: " + input);
        System.out.println("Vowels: " + vowels);
        System.out.println("Characters: " + length);
    }
}
