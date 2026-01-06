<?php 
    $sle = $_POST["id_eleve"];
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ajouter</title>
    <link rel="stylesheet" href="../../style.css">
</head>
<body>
    <main>
        
        <h1>Saisie des Notes</h1>
        
        <form action="modif/change.php" method="post">
            <fieldset>
                <legend>Les Notes</legend>
                <?php echo "<input type='hidden' name='id_eleve' value='$sle'>";?>
                

                <div class="formu">
                    <label for="NP">Nom Prenom : </label>
                    <input type="text" name="NP" id="NP">
                </div>
                <div class="formu">
                    <label for="Ndc">Note de controle : </label>
                    <input type="text" name="Ndc" id="Ndc">
                </div>
                <div class="formu">
                    <label for="Nds">Note de Synthése : </label>
                    <input type="text" name="Nds" id="Nds">
                </div>
                
                
                <div class="formu">
                    <button type="submit">Ajouter</button>
                    <button type="reset">Annuler</button>
                </div>
            </fieldset>
        </form>
    </main>
</body>
</html>
