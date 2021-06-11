public class Program
{
    public static void main(String[] args) {
		
        int [] arr =  {1 , 3 , 17 , 5, 6 ,0, 33, 11, 56, 69, 99 };
        int E=0, O =0;
        for(int i = 0; i < arr.length; i++){
            if(arr [i] % 2 == 0 )
                E++;
             
            else
            O++;
        }
        System.out.println("Number of Even: "+E+ "\nNumber of Odds: "+O);
	}
}
