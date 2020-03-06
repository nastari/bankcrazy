from classeConta import Conta 
from classeConexao import Conexao

class Operador():

    def start(self):

        def novaConta():

            conexao = Conexao()
            id = input('insira um id') # I know.
            nome = input('Insira seu nome:')
            cpf = input('Insira seu cpf')
            email = input('Insira seu email')
            contato = input('Insira seu telefone')

            conexao.registrarCliente(id,nome,cpf,email,contato)
           
        def login():
            pass

        print('Welcome to the Crazy Bank!')

        print('1 - New Client')

        print('2 - Login')

        escolha = int(input())

        if escolha == 1:
            novaConta()
        elif escolha == 2:
            login()
        else:
            self.start()





            

          



