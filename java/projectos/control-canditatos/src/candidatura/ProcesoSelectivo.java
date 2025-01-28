package candidatura;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;

public class ProcesoSelectivo {
    public static void main(String[] args) {
        String [] candidatos = {"FELIPE", "MARCIA", "JULIA", "PAULO", "AUGUSTO", "MONICA"};

        for (String candidato : candidatos) {
            entrandoEnContacto(candidato);
        }
    }

    static void entrandoEnContacto(String candidato) {
        int tentativasRealizadas = 1;
        boolean continuarIntentando = true;
        boolean atendio = false;

        do {
            atendio = atender();
            continuarIntentando = !atendio;

            if(continuarIntentando) {
                tentativasRealizadas ++;
            }System.out.println("CONTACTO REALIZADO CON " + candidato);

        }while(continuarIntentando && tentativasRealizadas<3);

        if(atendio) {
            System.out.println("CONTACTO REALIZADO CON " + candidato +  " EN " + tentativasRealizadas + " veces.");

        }else {
            System.out.println("NO PUDIMOS REALIZAR CONTACTO");
        }
    }

    // metodo auxiliar 
    static boolean atender() {
        return new Random().nextInt(3)==1;
    }

    static void imprimirSeleccionados() {
        String [] candidatos = {"FELIPE", "MARCIA", "JULIA", "PAULO", "AUGUSTO", "MONICA"};
        System.out.println("Imprimiendo el indice: ");
        
        for(int i=0; i < candidatos.length; i++) {
            System.out.println("El candidato de numero: " + (i+1) + " es: " + candidatos[i]);
        }

        System.out.println("Forma abreviada de interacion");

        for (String candidato : candidatos) {
            System.out.println("El candidato seleccionado es: " + candidato);
        }
    }

    static void seleccionCandidatos() {
        String [] candidatos = {"FELIPE", "MARCIA", "JULIA", "PAULO", "AUGUSTO", "MONICA"};

        int candidatosSeleccionados = 0;
        int candidatoActual = 0;
        double salarioBase = 2000.0;

        while (candidatosSeleccionados < 5 && candidatoActual < candidatos.length) {
            String candidato = candidatos[candidatoActual];
            double salarioPretendido = valorPretendido();

            System.out.println("El candidato " + candidato + " solicito este valor de salario " + salarioPretendido);

            if(salarioBase >= salarioPretendido) {
                System.out.println("El candidato " + candidato + " fue seleccionado.");
                candidatosSeleccionados ++;
            }
            candidatoActual ++;
        }
    }
    static double valorPretendido() {
        return ThreadLocalRandom.current().nextDouble(1800,2200);
    }
    static void analisarCandidato(double salarioPretendido) {
        double salarioBase = 2000.0;

        if(salarioBase > salarioPretendido) {
            System.out.println("Llamar para candidato");
        
        }else if(salarioBase == salarioPretendido) {
            System.out.println("Llamar a candidatos con contra propuesta");

        }else {
            System.out.println("Esperando mas candidatos");
        }
    }
}
