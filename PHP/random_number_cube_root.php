<!DOCTYPE html>
<html>
    <head>
        <title>Cube_Root</title>
    </head>
    <body>
        <style>
        body{
            text-align:center;
            font-size:1.5em;
            font-family:serif;
            background:#20B2AA;
        }
        </style>
    </body>
</html>

<?php
#Change the value of $n to any number
    $n=mt_rand(1, 1000);
    echo "Number: $n<br>Cube Root: ";
    echo round(cube_root($n),4);    echo "<br><br><br>This code generates a random number and calculate its cube root..☺️<br>You can change the value of \$n in the code to calculate cube root of any other number..👍";
//Binary search method to find cube root
#function to find absolute value of 
#$n-$m*$m*$m same as abs($n-$m*$m*$m);
    function Sub($n, $m) {
        if($n > $m*$m*$m)
            return ($n-($m*$m*$m));
        else
            return (($m*$m*$m)-$n);
    }
    #main function to find cube root 
    function cube_root($n) {
        if($n<0) { #to handle -ve values
            $n=-$n; echo "-"; }
        $a=0; #start
        $b=$n; #end 
        $e=0.0001; #set precision
        while (true) {
            $m=($a+$b)/2; #mid
            $p=Sub($n,$m); #abs value
#if $p<=$e (abs value is less or equal to
#precision) mid $m is our answer...
            if($p<=$e)
                return $m;
       #if not $p<=$e then check
            if(($m*$m*$m)>$n)
                $b=$m; #if true we set $b as mid and start the search again...
            else
                $a=$m; //else we set $a as mid and start search again...
        }
    }
?>
