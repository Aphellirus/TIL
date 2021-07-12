<?php
//header("Content-Type: text/json; charset=UTF-8");

//example 1

echo "<h3>Example 1 json_encode</h3>";

$cart = array(
  "ID" => 12345,
  "Name" => "You name",
  "Email" => "mail@example.com",
  "contents" => array(
    array(
      "productID" => 100,
      "productName" => "First",
      "quantity" => 1
    ),
    array(
      "productID" => 101,
      "productName" => "Second",
      "quantity" => 2
    )
  ),
  "Completed" => true
);
  
echo json_encode($cart);

//Example 2

echo "<h3>Example 2 json_decode</h3>";

$json='{"name":"Skail",
        "price":1500,
        "description":{
          "size":["S","M","L","XL"],
          "color":["red","grey","blue"]}}';
$Item = json_decode($json, true);

echo "name = ".$Item['name'];
echo "<br/>price = ".$Item['price'];
echo "<br/>desription size = ".$Item['description']['size'][1];
echo "<br/>description color = ".$Item['description']['color'][1];
?>
