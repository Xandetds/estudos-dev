import java.util.*;

public class exercicio07{
    public static void filtrarPares(ArrayList<Integer> numeros){

            ArrayList<Integer> numerosPares = new ArrayList<>();
            ArrayList<Integer> numerosImpares = new ArrayList<>();

            for (int numero : numeros){ 
                if (numero % 2 == 0){
                    numerosPares.add(numero);
                } else {
                    numerosImpares.add(numero);
                }
            }
            System.out.println("Numeros pares: " + numerosPares);
            System.out.println("Numeros impares: " + numerosImpares);

   
        }
        public static void main(String[] args) {
        ArrayList<Integer> numeros = new ArrayList<>();
        numeros.add(3);
        numeros.add(33);
        numeros.add(123);
        numeros.add(213123);
        numeros.add(35);
        numeros.add(43);
        numeros.add(34);
        numeros.add(44);

        filtrarPares(numeros);

        }
    }
