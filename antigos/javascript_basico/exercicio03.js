// OBJECTS

let person = {
name: 'xande',
age: 18
};

// da pra descobrir a propriedade colocando um ponto e vendo o que tem dentro
person.name = 'joao'

// tambem da com colchete mais usado quando nao sabe a variavel que vai usar e deixa o usuario escolher
let selection = 'name'
person[selection] = 'maria'


console.log (person.name);