//
// Crie uma função em JavaScript chamada 'filtrarPorLetraInicial' que receba
// um array de strings (palavras) e uma string `letraInicial` como argumentos.
//
// A função deve retornar um NOVO array contendo APENAS as palavras que começam
// com a `letraInicial` especificada.
//
// **Regras:**
// - A comparação deve ser case-insensitive.
// - Se o array de palavras estiver vazio, retorne um array vazio.

function filtrarPorLetraInicial(palavras, letraInicial) {
    const palavrasFiltradas = [];

    if (palavras.length === 0) {
        return [];
    }

    const letraInicialLowerCase = letraInicial.toLowerCase();

    for (let palavra of palavras) {
        if (palavra && palavra.toLowerCase().startsWith(letraInicialLowerCase)) {
            palavrasFiltradas.push(palavra);
        }
    }

    return palavrasFiltradas;
}

console.log(filtrarPorLetraInicial(["Maçã", "Banana", "Morango", "Manga"], "m"));
console.log(filtrarPorLetraInicial(["Cachorro", "Gato", "Coelho"], "g"));
console.log(filtrarPorLetraInicial([], "a"));
console.log(filtrarPorLetraInicial(["Abacaxi"], "A"));
