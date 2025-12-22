<?php
echo "Треугольные числа: <br>";
for ($n = 1; $n <= 10; $n++) {
    $treug[] = $n * ($n + 1) / 2;
}
echo implode("  ", $treug) . "<br>";

echo "Квадраты: <br>";
for ($n = 1; $n <= 10; $n++) {
    $kvd[] = $n * $n;
}
echo implode(" ", $kvd) . "<br>";

echo "Объединение: <br>";
$rez = array_merge($treug, $kvd);
print_r($rez);
echo "<br>";

echo "Сортировка: <br>";
sort($rez);
print_r($rez);
echo "<br>";

echo "Удаление первого элемента: <br>";
array_shift($rez);
print_r($rez);
echo "<br>";

echo "Удаление повторов: <br>";
$rez1 = array_unique($rez);
print_r($rez1);
?>
