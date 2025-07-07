/*

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mostrar/Ocultar Senha</title>
</head>
<body>
    <h1>Senha</h1>
    <input type="password" id="senha">
    <button onclick="alternarSenha()">Mostrar</button>
    </body>
</html>
*/

function alternarSenha() {
    let input = document.getElementById("senha");
    let botao = document.querySelector("button");
    if (input.type === "password") {
        input.type = "text";
        botao.innerText = "Ocultar";
    } else {
        input.type = "password";
        botao.innerText = "Mostrar";
    }
}