<?php
$link = mysqli_connect("localhost", "root", "root", "sales_db");

if (!$link) {
    die("Ошибка подключения к БД");
}

$sql_drop = "DROP TABLE IF EXISTS notebook";
mysqli_query($link, $sql_drop);

$sql_create = "
CREATE TABLE notebook (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    city VARCHAR(50),
    address VARCHAR(50),
    birthday DATE,
    mail VARCHAR(20)
)";

if (!mysqli_query($link, $sql_create)) {
    echo "Нельзя создать таблицу notebook";
} else {
    echo "Таблица notebook успешно создана";
}

mysqli_close($link);
?>
