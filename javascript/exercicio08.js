//
// Crie uma função em JavaScript chamada 'contarPropriedades' que receba
// um objeto como argumento.
//
// A função deve retornar o número total de propriedades (chaves) que o objeto possui.
//
// **Regras:**
// - Use um loop para percorrer as chaves do objeto.

function contarPropriedades(objeto) {
  let chaves = 0;

  for (let chave in objeto) {
    chaves++;
  }

  return chaves;
}

let pessoa = { nome: "xande", idade: 19, país: "islandia" };
console.log(contarPropriedades(pessoa)); 
