import java.util.stream.*;
public class Program
{
    public static void main(String[] args) {
        IntStream.range(1,11).forEach(System.out::println);
    }
}
