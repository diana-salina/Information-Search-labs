<?php
$cust = [
    "cnum"   => 2001,
    "cname"  => "Hoffman",
    "city"   => "London",
    "snum"   => 1001,
    "rating" => 100
];

print_r($cust);
echo "<br><br>";

echo "Сортировка по значениям: <br>";
asort($cust);
print_r($cust);
echo "<br><br>";

echo "Сортировка по ключам: <br>";
ksort($cust);
print_r($cust);
echo "<br><br>";

echo "sort(): <br>";
sort($cust);
print_r($cust);
?>
