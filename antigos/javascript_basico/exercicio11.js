/*

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Entrada Interativa</title>
</head>
<body>
    <p id="resultado"></p>
    <input type="text" id="entrada" placeholder="Digite algo..." oninput="digitarTexto()">
    </body>
</html>
*/

function digitarTexto() {
    let novoTexto = document.getElementById("entrada").value;
    document.getElementById("resultado").innerText = novoTexto;
}