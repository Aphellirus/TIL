import javax.swing.JOptionPane;
public class Main {
  
  public static void main(String[] args) {
  
    String name;
    name = JOptionPane.showInputDialog("Enter Your Name");
    JOptionPane.showMessageDialog(null, "Hello "+name);
    
    int age;
    age = Integer.parseInt(JOptionPane.showInputDialog("Enter Your age"));
    JOptionPane.showMessageDialog(null, "You are "+age+" years old");
  }
}
