//
// Crie um programa em Java que simule um caixa eletrônico.
//
// Regras:
// - Comece com um saldo inicial fixo.
// - Apresente um menu com as opções: consultar saldo, sacar valor e encerrar.
// - O saque deve diminuir o saldo apenas se houver valor suficiente.
// - O programa deve continuar exibindo o menu até que o usuário escolha encerrar.
//

interface Caixa{
    double consultarSaldo();
    void sacarValor(double valorSacado);
    void encerrar();
}

class CaixaEletronico implements Caixa{
    private double saldo = 4500;

    @Override
    public double consultarSaldo(){
        return saldo;
    }

    @Override
    public void sacarValor(double valorSacado){
        if (valorSacado <= saldo){
            saldo -= valorSacado;
            System.out.println("O valor sacado é de: "+ valorSacado + " e o novo valor na conta é de: " + saldo);
        }
    }
    @Override
    public void encerrar(){
        System.out.println("Uso do caixa encerrado!");
    }
}

public class exercicio04{
    public static void main(String[] args) {
        
    Caixa caixaXande = new CaixaEletronico();
    caixaXande.consultarSaldo();
    caixaXande.sacarValor( 1000.44);
    caixaXande.encerrar();
}
}