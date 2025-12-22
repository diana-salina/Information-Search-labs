<html> <head>

<title> Листинг 10-4. Обработка данных формы

        из листинга 10-3 </title> </head> <body>

<?php

class Person {

     private $name;

     private $hobbies;

    

     public function __construct($name, $hobbies) {

          $this->name = $name;

          $this->hobbies = $hobbies;

     }

    

     public function tellAboutHobbies() {

          print "<p>Меня зовут $this->name и я предпочитаю";

          print "<ul>\n";

          foreach ($this->hobbies as $hobby){

               print "<li>$hobby\n";

          }

          print "</ul>\n";

     }

}

 

    $user = $_POST["user"];

    $hobby = $_POST["hobby"];

    $nic = new Person($user, $hobby);

    $nic->tellAboutHobbies();

?>

 </body> </html>