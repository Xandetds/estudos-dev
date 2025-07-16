// exercicio05.js
//
// Crie uma função em JavaScript chamada 'calcularFatorial' que receba
// um número inteiro positivo como argumento.
//
// A função deve retornar o fatorial desse número.
//
// **Regras:**
// - O fatorial de 0 é 1.
// - O fatorial de um número negativo não é definido para este exercício (pode ignorar ou retornar uma mensagem de erro).

function calcularFatorial(n) {
  if (n < 0) {
    return "Fatorial não definido para número negativo";
  } else if (n === 0) {
    return 1;
  } else {
    let resultado = 1;
    for (let i = 1; i <= n; i++) {
      resultado *= i;
    }
    return resultado;
  }
}



console.log(calcularFatorial(5)); 
console.log(calcularFatorial(0)); 

