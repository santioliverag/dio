import java.util.InputMismatchException;
import java.util.Locale;
import java.util.Scanner;

public class AboutMe {

    public static void main(String[] args) {

        try {
            Scanner scanner =  new Scanner(System.in).useLocale(Locale.US);
        
            System.out.println("Digita tu nombre: ");
            String nombre = scanner.next();
    
            System.out.println("Digita tu apellido: ");
            String apellido = scanner.next();
    
            System.out.println("Digita tu edad: ");
            int edad = scanner.nextInt();
    
            System.out.println("Digita tu altura: ");
            Double altura = scanner.nextDouble();
    
    
            System.out.println("Hola, me llamo " + nombre.toUpperCase() + " " + apellido.toUpperCase());
            System.out.println("Tengo " + edad + " años");
            System.out.println("Mi altura es " + altura + "cm");

            scanner.close();
        }catch(InputMismatchException e) {
            System.err.println("Campos de edad y altura deben ser numericos");
        }
    }
}
