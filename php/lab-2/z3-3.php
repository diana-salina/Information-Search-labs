<?php
function Ru($color) {
    echo "<p style=\"color:$color;\">Здравствуйте!</p>";
}
function En($color) {
    echo "<p style=\"color:$color;\">Hello!</p>";
}
function Fr($color) {
    echo "<p style=\"color:$color;\">Bonjour!</p>";
}
function De($color) {
    echo "<p style=\"color:$color;\">Guten Tag!</p>";
}

$lang  = $_GET['lang'] ?? "";
$color = $_GET['color'] ?? "black";

if (function_exists($lang)) {
    $lang($color);
} else {
    echo "Неизвестный язык";
}
?>
