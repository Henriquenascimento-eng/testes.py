def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Exemplo de uso:
temperatura_c = float(input("Digite a temperatura em Celsius: "))
temperatura_f = celsius_para_fahrenheit(temperatura_c)
print(f"{temperatura_c}°C equivalem a {temperatura_f}°F")


