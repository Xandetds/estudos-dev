/*

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mostrar/Ocultar Elemento</title>
</head>
<body>
    <p id="textoEscondido">Este é um texto que pode ser ocultado!</p>
    <button id="alternarVisibilidade" onclick="alternarVisibilidade()">Ocultar</button>
    </body>
</html>
*/

function alternarVisibilidade() {
    let texto = document.getElementById("textoEscondido");
    let botao = document.getElementById("alternarVisibilidade");

    if (texto.style.display === "none") {
        texto.style.display = "block";
        botao.innerText = "Ocultar";
    } else {
        texto.style.display = "none";
        botao.innerText = "Mostrar";
    }
}