historico = []

def calcular():
    while True:
        print("\nCalculadora com Histórico")
        print("1. Somar (+)")
        print("2. Subtrair (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Ver Histórico")
        print("6. Sair")
        
        opcao = input("Escolha uma opção (1/2/3/4/5/6): ")
        
        if opcao == '6':
            print("Saindo...")
            break
        
        if opcao == '5':
            print("\n📜 Histórico de Cálculos:")
            for i, (operacao, resultado) in enumerate(historico, 1):
                print(f"{i}. {operacao} = {resultado}")
            continue
        
        if opcao not in ('1', '2', '3', '4'):
            print("Opção inválida!")
            continue
        
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida! Use números.")
            continue
        
        if opcao == '1':
            resultado = num1 + num2
            operacao = f"{num1} + {num2}"
        elif opcao == '2':
            resultado = num1 - num2
            operacao = f"{num1} - {num2}"
        elif opcao == '3':
            resultado = num1 * num2
            operacao = f"{num1} * {num2}"
        elif opcao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero!")
                continue
            resultado = num1 / num2
            operacao = f"{num1} / {num2}"
        
        historico.append((operacao, resultado))
        print(f"🔹 Resultado: {operacao} = {resultado}")

if __name__ == "__main__":
    calcular()