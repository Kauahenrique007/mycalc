import argparse

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        raise ValueError("Erro: Divisão por zero não é permitida.")
    return a / b

def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de linha de comando - realize operações matemáticas básicas.",
        epilog="Exemplo de uso: python calc.py somar 10 5"
    )
    subparsers = parser.add_subparsers(dest="operacao", help="Operações disponíveis")

    operacoes = {
        'somar': ('Soma dois números', somar),
        'subtrair': ('Subtrai o segundo número do primeiro', subtrair),
        'multiplicar': ('Multiplica dois números', multiplicar),
        'dividir': ('Divide o primeiro número pelo segundo', dividir)
    }

    for nome, (ajuda, _) in operacoes.items():
        oper_parser = subparsers.add_parser(nome, help=ajuda)
        oper_parser.add_argument("a", type=float, help="Primeiro número")
        oper_parser.add_argument("b", type=float, help="Segundo número")

    args = parser.parse_args()

    if args.operacao in operacoes:
        try:
            resultado = operacoes[args.operacao][1](args.a, args.b)
            print(f"Resultado da operação '{args.operacao}': {resultado}")
        except Exception as e:
            print(e)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
