import java.io.*;

class CreateFileTest
{
    public static void main(String args[])
    {
        try
        {
            if (new File("output.txt").createNewFile())
                System.out.println("Successfully created File.");

            else
                System.out.println("Failed to create file.");
        }
        catch (IOException e)
        {
            System.err.println(e.getMessage());
        }
    }
}
