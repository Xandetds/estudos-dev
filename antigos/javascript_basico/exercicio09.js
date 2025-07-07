/*

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mudar Cor do Fundo</title>
</head>
<body>
    <P id="cor">Clique para mudar de cor!</P>
    <button onclick="mudarCor()">Clique aqui</button>
    </body>
</html>
*/

function gerarCorAleatoria() {
    let letras = "0123456789ABCDEF";
    let cor = "#";
    for (let i = 0; i < 6; i++) {
        cor += letras[Math.floor(Math.random() * 16)];
    }
    return cor;
}

function mudarCor() {
    document.body.style.backgroundColor = gerarCorAleatoria();
    document.getElementById("cor").innerText = "Cor alterada pelo botão!";
}