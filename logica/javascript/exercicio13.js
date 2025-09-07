//
// Crie uma função em JavaScript chamada 'contarVogais' que receba
// uma string como argumento.
//
// A função deve retornar o número total de vogais (a, e, i, o, u) presentes na string.
//
// **Regras:**
// - A contagem deve ser case-insensitive (não diferenciar maiúsculas de minúsculas).


function contarVogais(string){
    let vogais = 'aeiouáéíóúàèìòùãõü'; 
    let contador = 0;    
    for (let letra of string) {
        letra = letra.toLowerCase();
        if (vogais.includes(letra)) { 
            contador += 1; 
        }
    }
    return contador; 
}

console.log(contarVogais("olá MUNDO")); 
console.log(contarVogais("JavaScript")); 
console.log(contarVogais("xande tibes"));