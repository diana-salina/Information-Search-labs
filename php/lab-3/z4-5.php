<?php
$list_sites = [
    "https://www.google.com",
    "https://www.yandex.ru",
    "https://www.yahoo.com"
];

$site = $_POST['site'] ?? "";

if ($site != "") {
    header("Location: $site");
    exit;
}
?>

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Перенаправление на выбранный сайт</title>
</head>
<body>

<form method="post">
    <select name="site">
        <?php
        $i = 0;
        while ($i < count($list_sites)) {
            echo "<option value='{$list_sites[$i]}'>{$list_sites[$i]}</option>";
            $i++;
        }
        ?>
    </select>
    <input type="submit" value="Перейти">
</form>

</body>
</html>
