<?php
$color = "blue";

echo "<table border=\"1\" cellpadding=\"5\">\n";

for ($i = 0; $i <= 10; $i++) {
    echo "\t<tr>\n";
    for ($j = 0; $j <= 10; $j++) {
        if ($i == 0 && $j == 0) {
            echo "\t\t<td style=\"color:red;\">+</td>\n";
        } elseif ($i == 0 || $j == 0) {
            echo "\t\t<td style=\"color:$color;\">".($i + $j)."</td>\n";
        } else {
            echo "\t\t<td>".($i + $j)."</td>\n";
        }
    }
    echo "\t</tr>\n";
}

echo "</table>";
?>
