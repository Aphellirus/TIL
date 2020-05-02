<?php
    $db = mysqli_connect("localhost","root","","ogloszenia") or die("Connection with database couldn't be done!"); //connection with database
    mysqli_set_charset($db,"utf-8"); //setting charset to data in database
    $query=mysqli_query($db,"SELECT * FROM `ogloszenie`") or die("Query trouble!"); //query to database
    echo '<table border="1">'; //beginning table
    while($result=mysqli_fetch_row($query)){ //getting results from database and setting them into loop
        echo "<tr>"; //beginning of row
        foreach($result as $key=>$value){ //loop for asociate arrays
            echo "<td>"; //beginning of cell
            echo $value." "; //printing data into table
            echo "</td>"; //ending of cell
        }
        echo "</tr>"; //ending of row
        //echo "<br>";
    }
    echo "</table>"; //table ending
    mysqli_close($db); //closing connection to database
?>
