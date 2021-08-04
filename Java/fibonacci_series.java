class MyClass {
    public static void main(String args[]) {
       int b=1; int c=0; int a=0;
         for(int i=0;i<=20;i++){
           if(i<=19){
           System.out.print(a+", ");
           c=a+b;
           a=b;
           b=c;
           
           
         } else{
             System.out.print(a+".");
           }
         }
    
        
    }
}
