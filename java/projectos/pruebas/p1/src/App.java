import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        
        Scanner scanner = new Scanner(System.in);

        // Entrada do saldo inicial
        double saldoInicial = scanner.nextDouble();
        double saldoFinal = 0;
        int i = 0;
        // TODO: Na linha abaixo, implemente a entrada das três transações:
        
        do {
          double transações = new scanner.nextDouble();
          saldoFinal = saldo + transações;
        }while(i<=3);

        // Saldo final
        System.out.printf("%.2f\n", saldoFinal);
    }
}
