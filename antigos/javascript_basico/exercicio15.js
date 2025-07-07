/*

<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contador com Teclado</title>
</head>
<body>
    <h1>Contador</h1>
    <p id="contador">0</p>
    </body>
</html>
*/

let contador = 0;
document.addEventListener("keydown", function(event) {
    if (event.key === "ArrowUp") {
        contador++;
    } else if (event.key === "ArrowDown") {
        contador--;
    }
    document.getElementById("contador").innerText = contador;
});