<?php
$link = mysqli_connect("localhost", "root", "root", "sales_db");
if (!$link) die("Ошибка подключения");

mysqli_set_charset($link, "utf8");

mysqli_query($link, "
INSERT INTO notebook (name, city, address, birthday, mail)
VALUES ('Иван Иванов', 'Москва', 'ул. Ленина, 1', '1999-05-10', 'ivan@mail.ru')
");

mysqli_query($link, "
INSERT INTO notebook (name, city, address, birthday, mail)
VALUES ('Анна Петрова', 'Санкт-Петербург', 'Невский пр., 10', '2000-12-01', 'anna@mail.ru')
");

mysqli_query($link, "
INSERT INTO notebook (name, city, address, birthday, mail)
VALUES ('Пётр Сидоров', 'Новосибирск', 'Красный проспект, 25', '1998-03-25', 'petr@mail.ru')
");

echo "Три записи добавлены";

mysqli_close($link);
?>
