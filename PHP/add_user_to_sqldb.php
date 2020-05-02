<?php

    //A fast way to add users to your database

    /*
    *This function can be modified depending on the amount of fields in your form
    *Pass in the first argument the object used to make the connection
    */

    //increase the number of arguments if you have more fields
    function add_user($connection, $firstName, $lastName, $username, $password)
    {                                                                            
        $stmt = $connection->prepare('INSERT INTO users VALUES(?,?,?,?)');
        $stmt->bind_param('ssss', $firstName, $lastName, $username, $password);
        $stmt->execute();
        $stmt->close();
    }

?>
