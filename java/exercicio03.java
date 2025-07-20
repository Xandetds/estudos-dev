//
// Crie um programa em Java que leia números inteiros positivos digitados pelo usuário
// e calcule a média dos números inseridos.
//
// **Regras:**
// - Utilize um laço `do-while` para continuar pedindo números até que o usuário digite um número negativo.
// - Ignore os zeros usando `continue` (não devem entrar na média).
// - Quando um número negativo for digitado, encerre o laço com `break` e exiba a média final.
//
import java.util.Scanner;

public class exercicio03 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int numero;
        int soma = 0;
        int contador = 0;

        do {
            System.out.print("Digite um número: ");
            numero = scanner.nextInt();

            if (numero == 0) {
                continue; 
            }

            if (numero < 0) {
                break; 
            }

            soma += numero;
            contador++;
        } while (true);

        if (contador > 0) {
            double media = (double) soma / contador;
            System.out.println("Média dos números inseridos: " + media);
        } else {
            System.out.println("Nenhum número válido foi inserido.");
        }

        scanner.close();
    }
}

