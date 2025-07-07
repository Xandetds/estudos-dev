/*

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contador de Tamanho</title>
</head>
<body>
    <p id="tamanho" style="font-size: 16px;">Tamanho: 16px</p>
    <button onclick="aumentarTamanho()">Aumentar Tamanho</button>
    <button onclick="diminuirTamanho()">Diminuir Tamanho</button>

    </body>
</html>
*/

let tamanhoFonte = 16;
function aumentarTamanho() {
    tamanhoFonte += 2;
    document.getElementById("tamanho").style.fontSize = tamanhoFonte + "px";
    document.getElementById("tamanho").innerText = "Tamanho: " + tamanhoFonte + "px";
}

function diminuirTamanho() {
    tamanhoFonte -= 2;
    document.getElementById("tamanho").style.fontSize = tamanhoFonte + "px";
    document.getElementById("tamanho").innerText = "Tamanho: " + tamanhoFonte + "px";
}