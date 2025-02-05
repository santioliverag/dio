package lanchonete;

public class Cozinheiro {
    public void adicionarLancheNoBalcao() {
        System.out.println("Adicionando lanche no balcao");
    }
    public void adicionarSucoNoBalcao() {
        System.out.println("Adicionando suco no balcao");
    }
    public void adicionarComboNoBalcao() {
        adicionarLancheNoBalcao();
        adicionarSucoNoBalcao();
    }

    public void prepararLanche() {
        System.out.println("Preparando lanche ");
    }

    public void prepararVitamina() {
        System.out.println("Preparando vitamina ");
    }

    public void pedirPraTrocarGas(Atendente meuAmigo) {
        meuAmigo.trocarGas();
    }
    public void pedirPraTrocarGas(Almoxarife meuAmigo) {
        meuAmigo.trocarGas();
    }
}
