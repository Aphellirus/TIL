<?php
$sentence = 'Say hello World one more time';
$sentence = implode(' ', array_reverse(explode(' ', $sentence)));
echo $sentence;
?>
