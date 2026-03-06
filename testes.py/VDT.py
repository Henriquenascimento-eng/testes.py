#FISICA (VDT)


def temp():
    dist1 = float(input("Digite a distancia em metros: "))
    vel1 = float(input("Digite a velocidade em Km/s: "))
    temp1 = dist1 * vel1
    print(f"Tempo em segundos: {temp1:.3f}")

def dist():
    temp2 = float(input("Digite a tempo em segundos: "))
    vel2 = float(input("Digite a velocidade em Km/s: "))
    dist2 = temp2 * vel2
    print(f"A distancia em metros/s: {dist2:.3f}")

def vel():
    temp3 = float(input("Digite a tempo em segundos: "))
    dist3 = float(input("Digite a distancia em metros: "))
    vel3 = dist3 / temp3
    print(f"Velocidade em Km/s: {vel3:.3f}")



def val(pergunta, inicio, fim):  # função para validar numeros inteiros
        while True:  # criando  loop infinito
            try:  # criando acordo/condição
                valor = int(input(pergunta))  # entrada de dados
                if inicio <= valor <= fim:  # determinando condição
                    return (valor)  # executa caso seja verdadeiro
                else:
                    return (0)
            except ValueError:  # executa caso seja falso
                print("valor invalido, favor digitar entre %d e %d" % (inicio, fim))


def menu():  # função que exibe o menu de opções
        print("""
       1- Descubra o tempo: 
       2- Descubra a distancia: 
       3- Descubra a velocidade: 
       4- sair do programa: 
    """)
        return val("Escolha uma opção: ", 1, 4)

while True:
    opcao = menu()
    if opcao >= 5:
        print("OPÇÃO INVALIDA")
    elif opcao == 1:
        temp()
    elif opcao == 2:
        dist()
    elif opcao == 3:
        vel()