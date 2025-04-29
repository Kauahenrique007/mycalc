class Calculadora:
    """
    Classe Calculadora que implementa operações matemáticas básicas
    com tratamento de erros e interface amigável.
    """
    
    @staticmethod
    def somar(a: float, b: float) -> float:
        """Realiza a adição de dois números."""
        return a + b
    
    @staticmethod
    def subtrair(a: float, b: float) -> float:
        """Realiza a subtração de dois números."""
        return a - b
    
    @staticmethod
    def multiplicar(a: float, b: float) -> float:
        """Realiza a multiplicação de dois números."""
        return a * b
    
    @staticmethod
    def dividir(a: float, b: float) -> float:
        """
        Realiza a divisão de dois números.
        Levanta ValueError se b for zero.
        """
        if b == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return a / b


def mostrar_menu() -> None:
    """Exibe o menu de opções da calculadora."""
    print("\n" + "="*40)
    print("CALCULADORA PROFISSIONAL".center(40))
    print("="*40)
    print("\nOperações disponíveis:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("0. Sair")
    print("="*40)


def obter_numero(mensagem: str) -> float:
    """
    Solicita um número ao usuário com tratamento de erro.
    
    Args:
        mensagem: Texto exibido para solicitar o número
        
    Returns:
        O número digitado pelo usuário
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Por favor, digite um número válido.")


def main() -> None:
    """Função principal que executa a calculadora."""
    calc = Calculadora()
    
    while True:
        mostrar_menu()
        
        try:
            opcao = int(input("\nDigite o número da operação desejada: "))
            
            if opcao == 0:
                print("\nObrigado por usar a Calculadora Profissional!")
                break
                
            if opcao not in range(1, 5):
                print("Opção inválida. Por favor, escolha uma operação de 1 a 4 ou 0 para sair.")
                continue
                
            num1 = obter_numero("Digite o primeiro número: ")
            num2 = obter_numero("Digite o segundo número: ")
            
            operacoes = {
                1: ("+", calc.somar),
                2: ("-", calc.subtrair),
                3: ("*", calc.multiplicar),
                4: ("/", calc.dividir)
            }
            
            simbolo, operacao = operacoes[opcao]
            
            try:
                resultado = operacao(num1, num2)
                print(f"\nResultado: {num1} {simbolo} {num2} = {resultado:.2f}")
            except ValueError as e:
                print(f"\nErro: {e}")
                
        except ValueError:
            print("Erro: Por favor, digite um número válido para a operação.")


if __name__ == "__main__":
    main()