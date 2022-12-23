<?php
$link = mysqli_connect("localhost", "root", "root", "sales_db");

if (!$link) {
    die("Ошибка подключения к БД");
}

if (!empty($_POST['name']) && !empty($_POST['mail'])) {
    $name = $_POST['name'];
    $city = $_POST['city'];
    $address = $_POST['address'];
    $birthday = $_POST['birthday'];
    $mail = $_POST['mail'];

    $sql = "INSERT INTO notebook (name, city, address, birthday, mail)
            VALUES ('$name', '$city', '$address', '$birthday', '$mail')";

    mysqli_query($link, $sql);
}
?>
<h2>Записная книжка</h2>

<form method="post">
    Введите фамилию и имя [*]: <input type="text" name="name"><br><br>
    Введите город: <input type="text" name="city"><br><br>
    Введите адрес: <input type="text" name="address"><br><br>
    Введите дату рождения в формате ГГГГ-ММ-ДД: <input type="text" name="birthday"><br><br>
    Введите e-mail [*]: <input type="text" name="mail"><br><br>
    <input type="submit" value="Записать!">
</form>

<a><br>Поля, помеченные [*], являются обязательными для заполнения</a>

<?php mysqli_close($link); ?>
