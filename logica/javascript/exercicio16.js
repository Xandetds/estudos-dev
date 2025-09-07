//
// Crie uma função em JavaScript chamada 'contarCaracteresUnicos' que receba
// uma string como argumento.
//
// A função deve retornar o número total de caracteres únicos presentes na string.
//
// **Regras:**
// - A contagem deve ser case-insensitive.
// - Espaços e pontuações devem ser ignorados.

function contarCaracteresUnicos(string) {
    let stringLimpa = string.toLowerCase();
    stringLimpa = stringLimpa.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
    stringLimpa = stringLimpa.replace(/[^a-z0-9]/g, "");

    const caracteresUnicos = new Set();

    for (let char of stringLimpa) {
        caracteresUnicos.add(char);
    }

    return caracteresUnicos.size;
}

console.log(contarCaracteresUnicos("Olá Mundo!"));
console.log(contarCaracteresUnicos("banana"));
console.log(contarCaracteresUnicos("Teste TEstE"));
console.log(contarCaracteresUnicos("Programação"));