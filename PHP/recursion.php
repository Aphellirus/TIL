<?php  
function factorial($n)  
{  
    if($n <= 1)   
    {  
        return 1;  
    }  
    else   
    {  
        return $n * factorial($n - 1);  
    }  
}  
  
echo "Factorial of 6 is " .factorial(5);  
?>  


