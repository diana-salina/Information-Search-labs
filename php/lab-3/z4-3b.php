<?php
$name = $_POST['name'] ?? "Без имени";

$otv = ["6","9","4","1","3","2","5","8","7"];

$right = 0;

for ($i = 1; $i <= 9; $i++) {
    if (isset($_POST["q$i"]) && $_POST["q$i"] === $otv[$i-1]) {
        $right++;
    }
}

echo "<h3>$name</h3>";
echo "Правильных ответов: $right<br><br>";

switch ($right) {
    case 9:
        echo "великолепно знаете географию";
        break;
    case 8:
        echo "отлично знаете географию";
        break;
    case 7:
        echo "очень хорошо знаете географию";
        break;
    case 6:
        echo "хорошо знаете географию";
        break;
    case 5:
        echo "удовлетворительно знаете географию";
        break;
    case 4:
        echo "терпимо знаете географию";
        break;
    case 3:
        echo "плохо знаете географию";
        break;
    case 2:
        echo "очень плохо знаете географию";
        break;
    default:
        echo "вообще не знаете географию";
}

echo "<br><a href='z4-3a.html'>Попробовать еще раз</a>";
?>
