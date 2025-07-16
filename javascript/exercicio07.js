//
// Crie uma função em JavaScript chamada 'filtrarNumerosPares' que receba
// um array de números inteiros como argumento.
//
// A função deve retornar um NOVO array contendo APENAS os números pares do array original.
//
// **Regras:**
// - O array original pode estar vazio.
// - Use um loop para percorrer o array.

function filtrarNumerosPares(numeros) {
  let pares = [];

  for (let i = 0; i < numeros.length; i++) {
    if (numeros[i] % 2 === 0) {
      pares.push(numeros[i]);
    }
  }

  return pares;
}

console.log(filtrarNumerosPares([1, 2, 3, 4, 5, 6, 77, 88]))