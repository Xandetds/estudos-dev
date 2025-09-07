import java.util.ArrayList;
import java.util.*;

public class exercicio09 {

    public static int contadorPalavras(List<String> lista, String palavra) {
        final String palavraLowerCase = palavra.toLowerCase(); 
        final List<String> listaLowerCase = new ArrayList<>();
        
        lista.forEach(p -> listaLowerCase.add(p.toLowerCase())); 

        int contador = 0;

        for (String p : listaLowerCase) {
            if (p.equals(palavraLowerCase)) { 
                contador++; 
            }
        }
        return contador; 
    }

    public static void main(String[] args) {
        ArrayList<String> lista = new ArrayList<>();
        lista.add("Alexandre");
        lista.add("Tibes");
        lista.add("da");
        lista.add("Silva");
        lista.add("Alexandre");
        lista.add("o");
        lista.add("grande");
        lista.add("Alexandre");
        lista.add("o");
        lista.add("da");

        String palavraBuscada = "o";
        int vezes = contadorPalavras(lista, palavraBuscada);
        System.out.println("A palavra '" + palavraBuscada + "' apareceu " + vezes + " vezes."); 
    }
}