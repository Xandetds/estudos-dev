//
// Crie um programa em Java que leia nomes digitados pelo usuário e informe a quantidade de caracteres de cada um.
//
// Regras:
// - Continue lendo nomes até que o usuário digite "fim".
// - O programa deve exibir o número de caracteres de cada nome digitado.
// - O programa deve encerrar imediatamente após o usuário digitar "fim".
//

import java.util.Scanner;



interface Leitor{
    String getNome(String nome);
    void contarCaracteres(String nome);
}

class LerInformacoes implements Leitor{
    @Override 
    public String getNome(String nome){
            return nome;
    }

    @Override
    public void contarCaracteres(String getNome){
     int caracteres = getNome.length();
            System.out.println("O numero de caracteres no nome é: " + caracteres);
}
}


public class exercicio05{
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Leitor nomeLeitor = new LerInformacoes();

        while(true){
        System.out.println("Digite um nome: ");
        String nome = scanner.nextLine();
        if (nome.equals("fim")) {
                System.out.println("Leitura encerrada, fim.");
                break;
            }
            

        nomeLeitor.getNome(nome);
        nomeLeitor.contarCaracteres(nome);
        }
        scanner.close();

    }
}
