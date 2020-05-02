

<?php 
$servername = "localhost";
$username = "username";
$password = "password";

//Create connection
$conn = new mysqli($servername, $username, $password);
// Check connection 
if($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
//create database
$sql = "CREATE DATABASE MYDB";
if ($conn->query($sql) === TRUE) {
    echo "Database create successfully";
} else {
    echo "Error creating database: " $conn->error;
}

$conn->close();
?>
