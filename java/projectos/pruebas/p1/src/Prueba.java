import java.util.Scanner;

public class Prueba {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Entrada do saldo inicial
        System.out.print("Digite o valor inicial: \n");
        double saldoInicial = scanner.nextDouble();
        double suma =0;
        double saldo = 0;

        
        for (int i = 1; i <= 3; i++) {
            System.out.print("Digite transaccion " + i + ": \n");
            double transacao = scanner.nextDouble();
            
            suma += transacao;
        }
        
        saldo = saldoInicial + suma;
        // Saldo final
        System.out.printf("%.2f\n", saldo);
        System.out.println("Suma: " + suma);
        scanner.close();

    }
}
