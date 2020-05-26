import java.util.ArrayList;
import java.util.Collections;

public class MyClass {
    public static void main(String[ ] args) {
        ArrayList<Integer> nums = new ArrayList<Integer>();
        nums.add(3);
        nums.add(36);
        nums.add(73);
        nums.add(40);
        nums.add(100);
        nums.add(1);
        nums.add(15);
        nums.add(17);
        nums.add(121);
        nums.add(178);
        
        Collections.sort(nums); // here we sort the numbers in ascending order
        System.out.println(nums);
    }
}
