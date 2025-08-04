public class exercicio06{
    public static void fizzBuzz(int a){
        if ((a % 3 == 0) && (a % 5 == 0)){
            System.out.println("FizzBuzz");
        } else if (a % 3 == 0) {
            System.out.println("Fizz");
        } else if (a % 5 == 0){
            System.out.println("Buzz");
        } else {
            System.out.println(a);
        }
    }
    public static void main(String[] args) {
         for (int i = 1; i <= 15; i++) {
            fizzBuzz(i);
    }
}
}