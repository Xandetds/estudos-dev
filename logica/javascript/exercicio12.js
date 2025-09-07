//
// Crie uma função em JavaScript chamada 'contarCaracteresTipo' que receba
// uma string `texto` e uma string `tipo` ('letras', 'numeros', 'espacos', 'especiais').
//
// A função deve retornar a quantidade de caracteres do tipo especificado na string.
//
// **Regras:**
// - Para 'letras', conte 'a' a 'z' e 'A' a 'Z'.
// - Para 'numeros', conte '0' a '9'.
// - Para 'espacos', conte ' '.
// - Para 'especiais', conte caracteres que não são letras, números ou espaços.
// - A função deve ser case-insensitive ao contar letras.


function contarCaracteresTipo(texto, tipo) {
    let contador = 0;
    let textoMinusculo = texto.toLowerCase();
    const caracteresEspeciaisPadrao = '!@#$%^&*()_+{}[]:;<>,.?/~`-="\'\\|';

    for (let char of textoMinusculo) {
        if (tipo === 'letras') {
            if (char >= 'a' && char <= 'z') {
                contador++;
            }
        } else if (tipo === 'numeros') {
            if (char >= '0' && char <= '9') {
                contador++;
            }
        } else if (tipo === 'espacos') {
            if (char === ' ') {
                contador++;
            }
        } else if (tipo === 'especiais') {
            if (caracteresEspeciaisPadrao.includes(char) && !((char >= 'a' && char <= 'z') || (char >= '0' && char <= '9') || char === ' ')) {
                contador++;
            }
        }
    }
    return contador;
}


let minhaString = "Olá Mundo 123! @#$ dasdasdasdasdsads";

let contagemLetras = contarCaracteresTipo(minhaString, 'letras');
console.log(contagemLetras);

let contagemNumeros = contarCaracteresTipo(minhaString, 'numeros');
console.log(contagemNumeros);

let contagemEspacos = contarCaracteresTipo(minhaString, 'espacos');
console.log(contagemEspacos);

let contagemEspeciais = contarCaracteresTipo(minhaString, 'especiais');
console.log(contagemEspeciais);