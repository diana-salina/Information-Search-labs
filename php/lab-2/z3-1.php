<?php
$diagColor = "#ffee00";

echo "<table border=\"1\" cellpadding=\"5\">\n";

$i = 1;
while ($i <= 10) {
    echo "\t<tr>\n";
    $j = 1;
    while ($j <= 10) {
        if ($i == $j) {
            echo "\t\t<td style=\"background:$diagColor;\">".($i*$j)."</td>\n";
        } else {
            echo "\t\t<td>".($i*$j)."</td>\n";
        }
        $j++;
    }
    echo "\t</tr>\n";
    $i++;
}

echo "</table>";
?>
