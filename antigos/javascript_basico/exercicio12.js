/*

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lista de Tarefas Simples</title>
</head>
<body>
    <h1>Lista de Tarefas</h1>
    <input type="text" id="novaTarefa" placeholder="Digite uma tarefa">
    <button id="adicionarTarefa" onclick="digitarTexto()">Adicionar</button>
    <ul id="listaTarefas"></ul>
    </body>
</html>
*/

function digitarTexto() {
    let novoTexto = document.getElementById("novaTarefa").value;

    if (novoTexto.trim() !== "") {
        let novaLi = document.createElement("li");
        novaLi.innerText = novoTexto;

        let botaoRemover = document.createElement("button");
        botaoRemover.innerText = "Remover";
        botaoRemover.style.marginLeft = "10px";

        botaoRemover.onclick = function() {
            novaLi.remove();
        };

        novaLi.appendChild(botaoRemover);
        document.getElementById("listaTarefas").appendChild(novaLi);
        document.getElementById("novaTarefa").value = "";
    }
}