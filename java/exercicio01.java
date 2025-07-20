//
// Crie um programa em Java que calcule a soma dos números de 1 a 100,
// pulando todos os múltiplos de 5.
//
// **Regras:**
// - Utilize um laço `for`.
// - Use a instrução `continue` para ignorar os múltiplos de 5.
// - Exiba a soma final no console.
//
public class exercicio01 {
    public static void main(String[] args) {
        var soma = 0;
            for (int i = 1; i <= 100; i++) {
            if (i % 5 == 0) {
                continue;
            }
            soma += i;
        }

        System.out.println("a soma final dos números de 1 a 100, ignorando múltiplos de 5, é: " + soma);
    }
}