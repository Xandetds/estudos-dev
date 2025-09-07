// exercicio06.js
//
// Crie uma função em JavaScript chamada 'encontrarMaiorNumero' que receba
// um array de números como argumento.
//
// A função deve retornar o maior número presente no array.
//
// **Regras:**
// - O array não estará vazio.
// - Não use o método `Math.max()` ou `.sort()` diretamente para encontrar o maior.
//   Faça a lógica de comparação manualmente com um loop.
//

function encontrarMaiorNumero(numeros) {
  let maior = numeros[0];  
  for (let i = 1; i < numeros.length; i++) {
    if (numeros[i] > maior) {
      maior = numeros[i]; 
    }
  }

  return maior;
}


let lista = [10, 45, 32, 87, 3];
console.log(encontrarMaiorNumero(lista)); 

console.log(encontrarMaiorNumero([1, 2, 3, 4, 5, 66]))