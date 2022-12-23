<?php
function vid_structure($table) {
    echo "<h4>Структура таблицы $table</h4>";

    $res = mysqli_query($GLOBALS['link'], "DESCRIBE `$table`");

    echo "<table border='1' cellpadding='5'>";
    echo "<tr><th>Поле</th><th>Тип</th><th>NULL</th><th>Ключ</th></tr>";

    while ($row = mysqli_fetch_row($res)) {
        echo "<tr>";
        echo "<td>$row[0]</td><td>$row[1]</td><td>$row[2]</td><td>$row[3]</td>";
        echo "</tr>";
    }
    echo "</table><br>";
}

function vid_content($table) {

    $rus_name = [
        "snum" => "№ продавца",
        "sname" => "Имя продавца",
        "comm" => "Комиссионные",
        "cnum" => "№ покупателя",
        "cname" => "Имя покупателя",
        "rating" => "Рейтинг",
        "onum" => "№ заказа",
        "amt" => "Сумма",
        "odate" => "Дата",
        "city" => "Город"
    ];

    echo "<h4>Содержимое таблицы $table</h4>";

    $res = mysqli_query($GLOBALS['link'], "SELECT * FROM `$table`");

    echo "<table border='1' cellpadding='5'>";

    $fields = mysqli_fetch_fields($res);
    echo "<tr>";
    foreach ($fields as $f) {
        $rus = $rus_name[$f->name] ?? "";
        echo "<th>$rus<br>{$f->name}</th>";
    }
    echo "</tr>";

    while ($row = mysqli_fetch_row($res)) {
        echo "<tr>";
        foreach ($row as $val) {
            echo "<td>$val</td>";
        }
        echo "</tr>";
    }

    echo "</table><br>";
}

if (isset($_GET['structure'])) {
    foreach ($_GET['structure'] as $table) {
        vid_structure($table);
    }
}

if (isset($_GET['content'])) {
    foreach ($_GET['content'] as $table) {
        vid_content($table);
    }
}

echo "<br><a href='z10-1.html'>Возврат к выбору таблицы</a>";
?>
