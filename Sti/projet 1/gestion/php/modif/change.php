<?php 
    require "../../conexion.php";
    $sel= $_POST["id_eleve"];
    //var_dump($_POST);
    $np = $_POST["NP"];
    $nc = $_POST["Ndc"];
    $ns = $_POST["Nds"];
    $nom = substr($np,0,strpos($np," "));
    $prenom = substr($np,strpos($np," ")+1);
    $req = "UPDATE Eleves SET Nom = '$nom', Prenom = '$prenom', NC = $nc, NS = $ns WHERE Id = '$sel'";
    $R = mysqli_query($cnx,$req) or die("Problemes d'insertion".mysqli_error($cnx));
?>