<html>
<head><title>sorting your data</title></head>
<body>
<h1>sorting your data</h1>
<?php

$connection=mysql_connect("localhost","root","")/*make sure you have a database as mention in this program*/
or die("couldn't connect to server");

$db=mysql_select_db("vmv", $connection)
or die("couldn't select database");

$query="SELECT * FROM snacks ORDER BY name";

$result=mysql_query($query)
or die("QUERY FAILED:" .mysql_error());

echo"<table border='1'>";
echo"<tr>";
echo"<th>NAME</th><th>NUMBER</th>";
echo"</tr>";

while($row=mysql_fetch_array($result))
{
    echo"<tr>";
echo"<td>",$row['name'],"</td><td>",$row['number'], "</td>";
echo"</tr>";
}
echo"</table>";
mysql_close($connection);
?>
</body>
</html>
