agenda = [] #Criando uma lista vazia 

#definindo funções 

#Descrição: este procedimento cria um novo contato
#Nome: novo()
#Tipo: procedimento
def novo(): 
    global agenda #definindo variavel como global 
    nome = p_nome()
    celular = input("celular...: ")
    email = input("email...: ")
    agenda.append([nome,celular,email]) #adicionando dados na agenda
    print("\n----------------------"
          "\nRegristro gravado com sucesso\n"
          "\n----------------------")
    

#Descrição: Este procedimento le nome
#Nome: p_nome()
#Tipo: procedimento
def p_nome():
    return(input("nome.....: "))


#Descrição: este procedimento lista todos regisros da matriz
#nome: lista_dados
#tipo: procedimento
def listar_dados(nome, celular, email):
    print("\nNome: %s\ncelular: %s\nemail: %s " % (nome, celular, email))
    print("--------------------------")

#Descrição: este procedimento lista todos registros da matriz
#nome: listar()
#tipo: procedimento
def listar(): #função para mostrar a lista de contatos
    print("\nCONTATOS DA AGENDA #####\n")
    for e in agenda: 
        listar_dados(e[0], e[1], e[2])
        print("\nFIM DA AGENDA #####\n")


#Descrição: Esta função pesquisa o contato pelo nome
#nome: pesquisa(nome): int
#tipo: função
def pesquisa(nome): #função registro de contato
    name = nome.lower()
    for d, e in enumerate(agenda): #percorre toda matriz
        if e(0).lower() == name: #procura o nome desejado
           return d #retorna o indice do nome encontrado
    return None #retorna vazio se não encontrar 


#Descrição: Este procedimento exibe o registro ou mensagem insucesso
#nome: pesquisar()
#tipo: procedimento
def pesquisa(): 
    #pesquisa o nome
    p = pesquisa(p_nome())  #entrada de dados
    if p != None: 
        print("Registro encontrado!")
        #atualizar as variaveis que encontrou
        nome = agenda[p][0]
        celular = agenda[p][1]
        email = agenda[p][2]
        #mostra o registro
        listar_dados(nome, celular, email)
    else:
        #exibe a mensagem de insucesso na procura do registro
        print("\nNome não encontrado!!")


#Descrição: Apagar o registro
#nome: apagar()
#tipo: procedimento
def apagar():
    global agenda
    nome = p_nome()
    #retorna o nome do indice do nome vazio
    p = pesquisa(nome)
    if p != None: #se encontrar o contato
        del agenda[p] #exclui o contato
        print("\n--------------------"
              "\nRegistro apagado com sucesso\n"
              "----------------------")
    else:
        #não encontrou o registro para excluir 
        print("nome não encontrado.")


#Descrição: Este procedimento edita contato 
#nome: editar()
#tipo: procedimento
def editar():
    p = pesquisa(p_nome()) #entrada de dados
    if p != None: 
        #mostra o nome e pede edição dos demais
        nome = agenda[p][0]
        print("Nome.....", nome)
        celular = input("celular...")
        email = input("email...")
        agenda[p] = [nome, celular, email] #armazenar novos dados
        print("\n-------------------"
              "\nRegistro editado com sucesso"
              "\n-------------------") 
    else: 
        print("Nome não encontrado") #executa caso seja falso


#Descrição: essa função valida se o item digitalizado foi valido
#nome: validar(pergunta, inicia, fim): int
#tipo: função
def validar(pergunta, inicio, fim): #função para validar numeros inteiros
    while True: #criando  loop infinito
        try: #criando acordo/condição
            valor = int(input(pergunta)) #entrada de dados
            if inicio <= valor <= fim: #determinando condição
                return (valor) #executa caso seja verdadeiro
            else:
                return (0)
        except ValueError: #executa caso seja falso
            print("valor invalido, favor digitar entre %d e %d" % (inicio, fim))


#Descrição: esta funçãoo retorna o item MENU ou 0 para invalido
#nome: menu(pergunta, inicio, fim): int
#tipo: função
def menu(): #função que exibe o menu de opções
    print("""
   1- Adicione novo contato
   2- Editar um contato
   3- Pesquisar contato
   4- Lista de contatos
   5- Apagar contato
   6- sair   
""")
    
    return validar("Escolha uma opção: ", 1, 6)

#PROGRAMA PRINCIPAL
while True: #criando um looop  infinito 
    opcao = menu()
    if opcao == 0:
        print("Opção Invalida")
    elif opcao == 6:
        break
    elif opcao == 1:
        novo()
    elif opcao == 2:
        editar()
    elif opcao == 3:
        pesquisa()
    elif opcao == 4:
        listar()
    elif opcao == 5:
        apagar()


     
