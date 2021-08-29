import java.util.*;
public class Program
{
    public static void main(String[] args) {
        Stack<Character> s1 = new Stack<>();
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        StringBuilder x = new StringBuilder();
        for(int i=0;i<s.length();i++) {
            s1.push((Character)s.charAt(i));
        }
        for(int i=0;i<s.length();i++) {
            x.append((char)s1.pop());
        }
        System.out.println(x);
    }
}
