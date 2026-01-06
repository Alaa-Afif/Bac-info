<?php
    require "../../conexion.php";
    //var_dump($_POST);
    $idd = $_POST["id_eleve"];
    $req = "DELETE FROM `Eleves` WHERE `Id` = '$idd'";
    $R = mysqli_query($cnx,$req) or die("there is a prooblem".mysqli_error($cnx));
    echo "success";
?>