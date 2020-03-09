from modelAccount import ( AccountClients , Session, session )

class Interface():


    def start(self):

        def novaConta():

            nome = input('Insira seu nome:')
            usuario = input('Seu usuario')
            senha = input('Sua senha')


            obj = AccountClients( name = nome , userLogin = usuario , passwordLogin = senha )
            session.add(obj)
            session.commit()
            
           
        def login():
            pass
            #usuario = input('Insira seu login')
            #senha = input('Insira sua senha')
            #conexao = Conexao()
            #conexao.login(usuario)

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

            

          



