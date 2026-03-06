nome = str(input("Digite seu nome: "))
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

IMC = peso / (altura * altura)

if IMC < 18.5:
     print(f"nome: {nome}\n "
           f"idade: {idade}\n "
           f"peso: {peso}\n "
           f"altura: {altura}\n"
           f"IMC: {IMC:.2f}, você está com o peso a baixo do normal")
elif IMC < 25:
     print(f"nome: {nome}\n "
           f"idade: {idade}\n "
           f"peso: {peso}\n "
           f"altura: {altura}\n"
           f"IMC: {IMC:.2f}, você está com o peso normal")
elif IMC < 30:
     print(f"nome: {nome}\n "
           f"idade: {idade}\n "
           f"peso: {peso}\n "
           f"altura: {altura}\n"
           f"IMC: {IMC:.2f}, você está com sobrepeso")
elif IMC < 40:
     print(f"nome: {nome}\n ")
     print(f"idade: {idade}\n ")
     print(f"peso: {peso}\n ")
     print(f"altura: {altura}\n ")
     print(f"IMC: {IMC:.2f}, você está obeso(a) ")