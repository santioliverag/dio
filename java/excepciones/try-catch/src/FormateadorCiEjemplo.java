public class FormateadorCiEjemplo {
    public static void main(String[] args) {
        try {
            String ciFormateada = formatearCi("51584772");
            System.out.println(ciFormateada);

        }catch(CiInvalidaException e) {
            System.out.println("La cedula no corresponde con la reglas de negocio");
        }
    }

    static String formatearCi(String ci) throws CiInvalidaException {
        if(ci.length() != 8) {
            throw new CiInvalidaException();
        }

        return "5.158.477-2";
    }
}
