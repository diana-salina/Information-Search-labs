<?php
$link = mysqli_connect("localhost", "root", "root", "sales_db");

if (!$link) {
    die("Ошибка подключения к БД");
}

$result = mysqli_query($link, "SELECT * FROM notebook");

echo "<table border=1>";
echo "<tr>
        <th>ID</th>
        <th>Имя</th>
        <th>Город</th>
        <th>Адрес</th>
        <th>Дата рождения</th>
        <th>E-mail</th>
      </tr>";

while ($row = mysqli_fetch_assoc($result)) {
    echo "<tr>";
    echo "<td>{$row['id']}</td>";
    echo "<td>{$row['name']}</td>";
    echo "<td>{$row['city']}</td>";
    echo "<td>{$row['address']}</td>";
    echo "<td>{$row['birthday']}</td>";
    echo "<td>{$row['mail']}</td>";
    echo "</tr>";
}

echo "</table>";

mysqli_close($link);
?>
