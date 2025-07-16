//
// Crie uma função em JavaScript chamada 'buscarObjetoPorPropriedade' que receba
// um array de objetos e duas strings: `chave` e `valor_buscado`.
//
// A função deve retornar o PRIMEIRO objeto do array que possui a `chave` especificada
// com o `valor_buscado`. Se nenhum objeto for encontrado, retorne `null`.
//
// **Regras:**
// - A busca deve ser case-sensitive para o valor.


function buscarObjetoPorPropriedade(arrayDeObjetos, chave, valor_buscado) {
    for (let objetoAtual of arrayDeObjetos) {
        if (objetoAtual.hasOwnProperty(chave) && objetoAtual[chave] === valor_buscado) {
            return objetoAtual; 
        }
    }
    return null;
}

let pessoas = [
    { id: 1, nome: "joao", idade: 30 },
    { id: 2, nome: "xande", idade: 25 },
    { id: 3, nome: "joao", idade: 35 }
];

let pessoaEncontrada1 = buscarObjetoPorPropriedade(pessoas, 'nome', 'xande');
console.log(pessoaEncontrada1);

let pessoaEncontrada2 = buscarObjetoPorPropriedade(pessoas, 'idade', 35);
console.log(pessoaEncontrada2);