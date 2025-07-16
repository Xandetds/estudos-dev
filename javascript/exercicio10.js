//
// Crie uma função em JavaScript chamada 'combinarArraysUnicos' que receba
// dois arrays como argumentos.
//
// A função deve retornar um NOVO array contendo todos os elementos dos dois arrays originais,
// mas sem duplicatas. A ordem dos elementos no array resultante não importa.
//
// **Regras:**
// - Use loops e condicionais, não métodos como `Set` ou `filter` avançado para remover duplicatas.

function combinarArraysUnicos(array1, array2) {
    let arrayCombinadoTemporario = array1.concat(array2);

    let arrayCombinado = []; 

    for (let elemento of arrayCombinadoTemporario) {
        if (!arrayCombinado.includes(elemento)) {
            arrayCombinado.push(elemento); 
        }
    }

    return arrayCombinado;
}


let numerosArray1 = [1, 2, 3, 2];
let numerosArray2 = [3, 4, 5, 1];
let resultadoNumeros = combinarArraysUnicos(numerosArray1, numerosArray2);
console.log(`Arrays de números combinados e únicos: [${resultadoNumeros}]`); 


let frutasArray1 = ["maçã", "banana", "uva"];
let frutasArray2 = ["banana", "laranja", "maçã"];
let resultadoFrutas = combinarArraysUnicos(frutasArray1, frutasArray2);
console.log(`Arrays de frutas combinados e únicos: [${resultadoFrutas}]`);