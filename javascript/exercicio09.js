//
// Crie uma função em JavaScript chamada 'reverterString' que receba
// uma string como argumento.
//
// A função deve retornar uma NOVA string com os caracteres da string original em ordem inversa.
//
// **Regras:**
// - Não use métodos como `.reverse()` ou `[...str].reverse().join('')`.
//   Faça a reversão usando um loop.


function reverterString(string) {
    let inversa = ""; 

    for (let i = string.length - 1; i >= 0; i--) {
        inversa += string[i]; 
    }

    return inversa; 
}


let palavraInvertida = reverterString("JavaScript");
console.log(`A palavra "JavaScript" invertida é: "${palavraInvertida}"`); 

let frase = "Olá mundo";
let fraseInvertida = reverterString(frase);
console.log(`A frase "${frase}" invertida é: "${fraseInvertida}"`);  