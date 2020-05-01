#include <stdio.h>
#include <stdlib.h>
#include <time.h>


int main()
{
  int u=0,c=0;
  
  int count=1;
  int usr=0,comp=0; 
  char str[][20]={"","STONE","PAPER","SCISSOR" };

  srand(time(NULL));
  
 
 
  
  while(count<=3)
  {
   
  
  printf("__________________________________\n");
  printf("ROUND = %d\n",count);
  printf("****USER TURN****");
  printf("\nInputs available\n 1 for STONE \n 2 for PAPER \n 3 for SCISSOR\n");
  printf("___________________________________\n");
  scanf("%d",&usr);
  printf("\nUSER INPUT\n");
 
  printf("\nUser Entered = %s \n",str[usr]);
  
  printf("___________________________________\n");
  printf("\n----COMPUTER TURN----");
  printf("\nInput\n 1 for STONE \n 2 for PAPER \n 3 for SCISSOR\n");
    comp=rand()%3+1;

printf("\n___________________________________\n");
 



  printf("\nCOMPUTER INPUT \n\n");
  printf("\Computer  Entered = %s \n",str[comp]);
  printf("___________________________________\n");
 

  
  printf("\n");
  
  if( (usr==1 && comp==3) ||  (usr==2 && comp==1) || (usr==3 && comp==2)  )
  {
    printf("\n User won this round = %d \n",count);
    u++;
  }
  else if(usr==comp)
  {
    printf("\nRound %d is DRAW\n",count);
      
  }
  else
  {
    printf("\n Computer won this round = %d \n",count);
    c++; 
    
  }
   
    count++;
  }
 
  
  if(u>c)
  {
    printf("\n\n*****USER WON THE GAME******\nPoints=%d\n",u);
  }
  else if(c>u)
  {
    printf("\n\n*****COMPUTER WON THE GAME******\nPoints=%d\n",c);
  }
  else
  {
    printf("\nGAME DRAW\n");
  }
  return 0;
}
