/*

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gerador de Números</title>
</head>
<body>
    <h1>Gerador de Números Aleatórios</h1>
    <button onclick="gerarNumero()">Gerar Número</button>
    <p id="numero"></p>
    </body>
</html>
*/

function gerarNumero() {
    let numero = Math.floor(Math.random() * 100) + 1;
    document.getElementById("numero").innerText = numero;
}