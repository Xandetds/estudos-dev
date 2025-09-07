//
// Crie uma função em JavaScript chamada 'ehPalindromo' que receba
// uma string como argumento.
//
// A função deve retornar `true` se a string for um palíndromo (lê-se igual de trás para frente),
// e `false` caso contrário.
//
// **Regras:**
// - Considere apenas letras e números. Ignore espaços, pontuações e maiúsculas/minúsculas.

function ehPalindromo(stringOriginal) { 
    let stringLimpa = stringOriginal.toLowerCase().replace(/[^a-z0-9]/g, "");

    let inversa = '';
    for (let i = stringLimpa.length - 1; i >= 0; i--) {
        inversa += stringLimpa[i];
    }
    if (stringLimpa === inversa) {
        return true; 
    } else {
        return false; 
    }
}

let palavra1 = 'arara'
let palavra2 = 'alexandre'
let frase1 = 'Ame o poema';

console.log(ehPalindromo(palavra1))
console.log(ehPalindromo(palavra2))
console.log(ehPalindromo(frase1))