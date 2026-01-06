<?php
    //connect

    $cnx = mysqli_connect("127.0.0.1","root","","Gestion_notes") or die("Probléme de connexion à MySql :".mysqli_connect_error($cnx));

    $id = $_POST["ID"];
    $np = $_POST["NP"];
    $nc = $_POST["Ndc"];
    $ns = $_POST["Nds"];

    $nom = substr($np,0,strpos($np," "));
    $prenom = substr($np,strpos($np," ")+1);
    $req = "INSERT INTO eleves (Id, Nom, Prenom, NC, NS)  VALUES ($id, '$nom', '$prenom', $nc, $ns)";
    $R = mysqli_query($cnx,$req) or die("Problemes d'insertion".mysqli_error($cnx));


    echo "Success";


?>