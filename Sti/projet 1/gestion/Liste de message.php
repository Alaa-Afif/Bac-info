<?php 
    require "conexion.php";
    $req = "SELECT * FROM Eleves";
    echo "<table border='1'>";
    echo "<tr>";
    echo "<th>Nom et Prenom</th>";
    echo "<th>Moyenne</th>";
    echo "</tr>";
    $res = mysqli_query($cnx,$req);
    while($li = mysqli_fetch_array($res)){
        $moy = ((($li["NS"]*2)+$li["NC"])/2);
        echo "<tr> ";
        echo "<td>".$li["Nom"]." ".$li["prenom"]."</td>";
        echo "<td>".$moy."</td>";
        echo "</tr>";
    }
    echo "</table>";

?>