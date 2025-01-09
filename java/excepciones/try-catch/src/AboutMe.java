import java.util.Locale;
import java.util.Scanner;

public class AboutMe {

    public static void main(String[] args) {

        Scanner scanner =  new Scanner(System.in).useLocale(Locale.US);
        
        System.out.println("Digita tu nombre: ");
        String nombre = scanner.text();

        System.out.println("Digita tu apellido: ");
        String apellido = scanner.nextLine();

        System.out.println("Digita tu edad: ");
        int edad = scanner.nextInt();

        System.out.println("Digita tu altura: ");
        Double altura = scanner.nextDouble();



    }
}
