import java.util.*;
import java.io.*;
import java.util.Scanner;

public class GameLauncher
{
    public static void main(String[] args) {
        GuessGame game = new GuessGame();
        game.start();
    }
}

public class Player
{   
 public int playerNum;
    private int inum=0;
    boolean Human=false;
    public void guess()
    {
    if (Human){
    Scanner sc = new Scanner(System.in);
     try {
        inum= sc.nextInt();
     }catch(Exception e)
     {
        System.out.println("INPUT ERROR") ;
     }
    } else{
    inum= (int)(Math.random()*10);
    }
    System.out.println("Guessing "+inum);      
    }
    public int GetGuess(){
        return inum ;
    }
}

public class GuessGame
{
final static int NumPlayers=3;

 public void start(){
 
 int iTarget = (int) (Math.random()*10);
 
    System.out.println("Number to guess is "+ iTarget );
    
     Player[] arrPlayers= new Player[NumPlayers];
    for (int i=0;i<NumPlayers;i++)
    {
    arrPlayers[i]= new Player();
    if (i==0){
      arrPlayers[i].Human=true; 
    }
    arrPlayers[i].guess();
    arrPlayers[i].playerNum=i;
    }
    

    boolean Winner = false;
    for (int i=0;i<NumPlayers;i++){
    if (arrPlayers[i].GetGuess() == iTarget)
    {
        System.out.println("We have a winner!");
        System.out.println("Player/s "+(arrPlayers[i].playerNum+1)+ " won!");
        System.out.println("GAME OVER");
        Winner=true;
        break;
    }
    }
    if (! Winner){
        System.out.println("No winner :(");

} 

}
}



