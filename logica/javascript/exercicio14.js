//
// Crie uma função em JavaScript chamada 'somarArray' que receba
// um array de números como argumento.
//
// A função deve retornar a soma de todos os elementos no array.
//
// **Regras:**
// - O array pode conter números positivos, negativos ou zero.
// - O array pode estar vazio, neste caso, retorne 0.


function somarArray(numeros){
    if (numeros.length === 0) {
        return 0; 
    }
    let soma = 0; 
    for (let numero of numeros) {
        soma += numero; // <-- Esta linha agora está DENTRO do loop e será executada para cada 'numero'.
    }
    return soma;
}


console.log(somarArray([1, 2, 3]));      
console.log(somarArray([-1, 5, 0]));    
console.log(somarArray([]));           
console.log(somarArray([10]));