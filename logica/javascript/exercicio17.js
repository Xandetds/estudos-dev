//
// Crie uma função em JavaScript chamada 'calcularMediaNotas' que receba
// um array de números (representando notas) como argumento.
//
// A função deve retornar a média aritmética de todas as notas no array.
//
// **Regras:**
// - Se o array estiver vazio, retorne 0 para evitar divisão por zero.

function calcularMediaNotas(notas) {
    if (notas.length === 0) {
        return 0;
    }

    let soma = 0;
    for (let i = 0; i < notas.length; i++) {
        soma += notas[i];
    }

    const media = soma / notas.length;
    return media;
}

console.log(calcularMediaNotas([10, 20, 30]));
console.log(calcularMediaNotas([70, 80, 90, 100]));
console.log(calcularMediaNotas([]));
console.log(calcularMediaNotas([50]));