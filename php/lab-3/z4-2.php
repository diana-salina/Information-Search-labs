<?php
$align  = $_GET['align']  ?? "left";
$valign = $_GET['valign'] ?? "top";
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Самообрабатывающаяся форма</title>
</head>
<body align="center">

<table border="1" width="100" height="100" align="center">
    <tr>
        <td align="<?= $align ?>" valign="<?= $valign ?>">Текст</td>
    </tr>
</table>

<form method="get">
    <p>Align:</p>
    <input type="radio" name="align" value="left"   <?= $align=="left"?"checked":"" ?>> left
    <input type="radio" name="align" value="center" <?= $align=="center"?"checked":"" ?>> center
    <input type="radio" name="align" value="right"  <?= $align=="right"?"checked":"" ?>> right

    <p>Valign:</p>
    <input type="checkbox" name="valign" value="top"    <?= $valign=="top"?"checked":"" ?>> top
    <input type="checkbox" name="valign" value="middle" <?= $valign=="middle"?"checked":"" ?>> middle
    <input type="checkbox" name="valign" value="bottom" <?= $valign=="bottom"?"checked":"" ?>> bottom
    <br><br>
    <input type="submit" value="Выполнить">
</form>

</body>
</html>
