/*

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List Melhorado</title>
</head>
<body>
    <h1>Lista de Tarefas</h1>
    <input type="text" id="novaTarefa" placeholder="Digite uma tarefa">
    <button onclick="adicionarTarefa()">Adicionar</button>
    <ul id="listaTarefas"></ul>
    </body>
</html>
*/

function adicionarTarefa() {
    let novaTarefaTexto = document.getElementById("novaTarefa").value;

    if (novaTarefaTexto.trim() !== "") {
        let lista = document.getElementById("listaTarefas");

        let novoItem = document.createElement("li");
        novoItem.innerText = novaTarefaTexto;

        let botaoConcluir = document.createElement("button");
        botaoConcluir.innerText = "Concluir";
        botaoConcluir.onclick = function () {
            if (novoItem.style.textDecoration === "line-through") {
                novoItem.style.textDecoration = "none";
                novoItem.style.color = "black";
            } else {
                novoItem.style.textDecoration = "line-through";
                novoItem.style.color = "gray";
            }
        };

        novoItem.appendChild(botaoConcluir);
        lista.appendChild(novoItem);

        document.getElementById("novaTarefa").value = "";
    }
}