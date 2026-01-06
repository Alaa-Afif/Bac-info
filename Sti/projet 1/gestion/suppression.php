<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajouter</title>
    <link rel="stylesheet" href="../style.css">
</head>
<body>
    <main>
        <h1>Modifier Les Notes</h1>

        <form action="php/supp/sup.php" method="post">
            <fieldset>
                <legend>Les eleve a supprimer</legend>
                <div class="formu">
                    <label for="">ID : </label>
                    <select name="id_eleve" id="id_eleve">
                        <?php
                            require "conexion.php";
                            
                            echo "<option value=''>-- Choisir un élève --</option>";
                            $req= "SELECT Id FROM Eleves ";
                            $ids = mysqli_query($cnx,$req) or die("Probleme de recherche de données : ".mysqli_error($cnx));
                            
                            while($row = mysqli_fetch_array($ids)){
                                echo "<option value = '".$row["Id"]."'>".$row["Id"]."</option>";
                            }
                        ?>
                    </select>
                </div>
                
                <div class="formu">
                    <button type="submit">Supprimer</button>
                    <button type="reset">Annuler</button>
                </div>
            </fieldset>
        </form>
    </main>
</body>
</html>
