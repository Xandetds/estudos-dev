//
// Crie um programa em Java que simule um sistema de login com até 3 tentativas.
//
// **Regras:**
// - O login correto é "admin" e a senha é "123".
// - Utilize um laço `while` para permitir até 3 tentativas do usuário.
// - Se o login for bem-sucedido, exiba uma mensagem de boas-vindas e interrompa o laço usando `break`.
// - Se atingir 3 tentativas incorretas, exiba "Acesso bloqueado".
//
import java.util.Scanner;

public class exercicio02 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int tentativas = 0;

        while (tentativas < 3) {
            System.out.print("Digite seu login: ");
            String login = scanner.nextLine();

            System.out.print("Digite sua senha: ");
            String senha = scanner.nextLine(); 
            if (login.equals("admin") && senha.equals("123")) {
                System.out.println("Bem-vindo, admin!");
                break;
            } else {
                tentativas++;
                System.out.println("Login ou senha incorretos.");
            }

            if (tentativas == 3) {
                System.out.println("Acesso bloqueado.");
            }
        }

        scanner.close();
    }
}
