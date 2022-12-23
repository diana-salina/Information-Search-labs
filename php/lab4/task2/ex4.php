<?php
$link = mysqli_connect("localhost", "root", "root", "sales_db");
if (!$link) die("Ошибка подключения");

$id = $_POST['id'] ?? null;
$field_name = $_POST['field_name'] ?? null;
$field_value = $_POST['field_value'] ?? null;

if ($id && $field_name) {
    $sql = "UPDATE notebook 
            SET $field_name = '$field_value'
            WHERE id = '$id'";
    mysqli_query($link, $sql);
}
?>

<form method="post">
<table border="1">
<tr>
    <th>id</th>
    <th>name</th>
    <th>city</th>
    <th>address</th>
    <th>birthday</th>
    <th>mail</th>
    <th>исправить</th>
</tr>

<?php
$result = mysqli_query($link, "SELECT * FROM notebook");
while ($a_row = mysqli_fetch_array($result)) {
?>
<tr>
    <td><?= $a_row['id'] ?></td>
    <td><?= $a_row['name'] ?></td>
    <td><?= $a_row['city'] ?></td>
    <td><?= $a_row['address'] ?></td>
    <td><?= $a_row['birthday'] ?></td>
    <td><?= $a_row['mail'] ?></td>
    <td>
        <input type="radio" name="id" value="<?= $a_row[0] ?>">
    </td>
</tr>
<?php } ?>
</table>

<br>
<input type="submit" value="Выбрать">
</form>

<?php
if ($id && !$field_name) {
    $res = mysqli_query($link, "SELECT * FROM notebook WHERE id='$id'");
    $a_row = mysqli_fetch_assoc($res);
?>
<br>

<form method="post">
<select name="field_name">
    <option value="name"><?= $a_row['name'] ?></option>
    <option value="city"><?= $a_row['city'] ?></option>
    <option value="address"><?= $a_row['address'] ?></option>
    <option value="birthday"><?= $a_row['birthday'] ?></option>
    <option value="mail"><?= $a_row['mail'] ?></option>
</select>

<a> введите новое значение: </a>

<input type="text" name="field_value">
<input type="hidden" name="id" value="<?= $id ?>">
<br>
<input type="submit" value="Заменить">
</form>

<?php } ?>

<br>
<a href="ex3.php">Посмотреть результат</a>

<?php mysqli_close($link); ?>
