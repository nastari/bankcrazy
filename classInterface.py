from modelAccount import ( AccountClients , Session, session )
from Transactions import ( Transactions )

class Interface():

    def start(self):


        def novaConta():

            nome = input('Insira seu nome:')
            usuario = input('Seu usuario')
            senha = input('Sua senha')


            obj = AccountClients( name = nome , userLogin = usuario , passwordLogin = senha )
            session.add(obj)
            session.commit()

        def painel(user):
            if (user):          
                print ()
                print ('  ###### Bank of Crazy ########')
                print ()
                print ('  Bem vindo: ' + user.name )
                print ()
                print ('  1- Verificar Saldo')
                print ('  2- Realizar Transferencia')
                print ('  3- Extrato')
                print ('  4- Empréstimos')
                print ()
                print ('  ############################')
            else: 
                print("Error.")
                self.start()    
            escolha = int(input('Opção: '))
            if ( escolha  == 2):

                def InterfaceTransfer():
                    print('#### OPERAÇÃO DE TRANSFÊRENCIA BANCÁRIA ######')
                    destiny = input('Para qual conta deseja enviar? R: ')
                    value = int(input('Qual valor da transferência? R: '))
                    if ( value >= 0):
                        transaction = Transactions(user,destiny,value)
                        transaction.transfer()
                    else:
                        print('Operação cancelada.')
                
                InterfaceTransfer()


        def login():
            pass
            usuario = input(' Insira seu login : ')
            senha = input(' Insira sua senha : ')

            filt = session.query(AccountClients).filter_by(userLogin= usuario).first() 
            if (filt):
                if( filt.passwordLogin == senha):
                    painel(filt)
                else:
                    self.start()
            else:
                print("Acesso negado. Verifique suas informações de login.")

        print()

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

            

          



