// 3-
// No index.html:
/*
    <p id="mensagem">Clique no botão para mudar o texto.</p>
    <button onclick="mudarTexto()">Clique aqui</button>
*/

// No Index.js
document.getElementById("mensagem").innerText = "Texto alterado ao carregar a página!";

function mudarTexto() {
    document.getElementById("mensagem").innerText = "Texto alterado pelo botão!";
}