import java.util.*;

public class exercicio08 {
    public static void main(String[] args) {
        
        List<Integer> numeros = Arrays.asList(1, 2, 3, 4, 5, 66, 76, 776, 54353);
        List<Integer> numerosPares = new ArrayList<>();
        List<Integer> numerosImpares = new ArrayList<>();


        numeros.forEach(numero -> { 
            if (numero % 2 == 0) { 
                numerosPares.add(numero);
            }
        });

         numeros.forEach(numero -> { 
            if (numero % 2 != 0) { 
                numerosImpares.add(numero);
            }
        });
        
        System.out.println("Pares: " + numerosPares);
        System.out.println("Impares: " + numerosImpares);
    }
    
}
