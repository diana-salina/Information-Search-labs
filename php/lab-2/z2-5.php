<?php
$lang = $_GET['lang'] ?? "";

if ($lang == "ru") {
    echo "русский";
} elseif ($lang == "en") {
    echo "английский";
} elseif ($lang == "fr") {
    echo "французский";
} elseif ($lang == "de") {
    echo "немецкий";
} else {
    echo "язык неизвестен";
}
?>
