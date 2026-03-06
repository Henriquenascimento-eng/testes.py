real = float(input("Digite um valor em real: "))
dolar = float(input("Digite a cotação do dólar: "))

def calculadora1(real, dolar):
    return real / dolar

conversor = calculadora1(real, dolar)
print(f"Você possui {conversor:.2f} dólares")

