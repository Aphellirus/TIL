import java.util.Arrays
   
open class ABC{  
    fun code (){
    
        print("Hey!! i am coding ")
    } 
} 
class BCD: ABC(){     

}  
fun main(args: Array<String>) {
    var  a=BCD()
    a.code() 
    
}
