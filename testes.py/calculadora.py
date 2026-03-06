# calculadora.py


def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não permitida.")
    return a / b

def potencia(a, b):
    return a ** b

def calculadora():
    operacoes = {
        "1": ("+", soma),
        "2": ("-", subtracao),
        "3": ("*", multiplicacao),
        "4": ("/", divisao),
        "5": ("**", potencia)
    }

    print("=== Calculadora Python ===")
    print("Operações disponíveis:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    print("5 - Potência (**)")
    print("6 - Sair")

    while True:
        opcao = input("\nEscolha uma opção (1–6): ")

        if opcao == "6":
            print("Encerrando a calculadora...")
            break

        if opcao not in operacoes:
            print("Opção inválida.")
            continue

        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))

            simbolo, funcao = operacoes[opcao]
            resultado = funcao(n1, n2)

            print(f"\n{n1} {simbolo} {n2} = {resultado:.2f}")

        except ValueError:
            print("Erro: digite apenas números válidos.")
        except ZeroDivisionError as e:
            print(f"Erro: {e}")

# Executar
calculadora()