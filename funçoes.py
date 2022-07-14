from time import sleep


def escolher():
    print('''
              [1]   - Cadastrar cliente 
              [2]   - Alterar cliente 
              [3]   - Excluir cliente 
              [4]   - Cadastrar produto 
              [5]   - Alterar produto 
              [6]   - Excluir produto 
              [7]   - Cadastrar venda 
              [8]   - Alterar venda 
              [9]   - Excluir venda 
              [10]  - Listar clientes 
              [11]  - Listar produtos 
              [12]  - Listar vendas 
              [13]  - Sair do programa 
              ''')
    opcao = input('Digite a opção desejada: ')
    return opcao

def validar_Cpf():
    validaCPF = True
    while validaCPF:
        cpf = input('Digite o CPF do cliente: ')
        if len(cpf) != 11:
            print('CPF inválido!')
            sleep(1)
            continue
        else:
            cpfReal = cpf
            totala = 0
            totalb = 0
            cont = 0
            b = 10
            a = 0
            cpf = ' '.join(filter(str.isalnum, cpf))
            cpf = cpf.split()


        while cont < 9:
            totala = totala + int(cpf[a]) * b
            a += 1
            b -= 1
            cont += 1
        cont = 0
        b = 11
        a = 0
        while cont < 10:
            totalb = totalb + int(cpf[a]) * b
            a += 1
            b -= 1
            cont += 1
        p1 = (totala * 10) % 11
        p2 = (totalb * 10) % 11
        if p1 == int(cpf[9]) and p2 == int(cpf[10]):
            validaCPF = False
            sleep(1)
            return cpfReal
        else:
            print("Digite um CPF válido!")




