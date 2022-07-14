import sqlite3
import requests
from funçoes import validar_Cpf

conexao = sqlite3.connect('Controle2.db')
cursor = conexao.cursor()


def ifo_Cliente():
    nome = input('Digite o nome do cliente: ')
    idade = int(input('Digite a idade do cliente: '))
    cpf = validar_Cpf()
    cep = input('Digite o cep do cliente: ')
    numero = int(input('Digite o numero do cliente: '))
    cliente = Cliente(nome, idade, cpf, cep, numero)
    cliente.Cadastrar_Cliente()


class Cliente:
    def __init__(self, nome, idade, cpf,  cep, numero):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.cep = cep
        self.numero = numero


    def Cadastrar_Cliente(self):
        response = requests.get('https://viacep.com.br/ws/%s/json/' % self.cep)
        response_json = response.json()
        cursor.execute('INSERT INTO Clientes (nome, idade, cpf, cep, rua, estado, cidade, bairro, numero) VALUES (?, '
                       '?, ?, ?, ?, ?, ?, ?, ?)',
                       (self.nome, self.idade,self.cpf, self.cep, response_json['logradouro'], response_json['uf'],
                        response_json['localidade'], response_json['bairro'], self.numero))
        conexao.commit()
        print('Cliente cadastrado com sucesso!')


