from modelAccount import ( AccountClients , Session, session )


class Transactions:
    
    def __init__(self, user, destiny, value ):
        self.user = user
        self.destiny = destiny
        self.value = value

    def transfer(self):
        destino = session.query(AccountClients).filter_by(userLogin= self.destiny).first() 
        if (destino and self.user != destino ):
            if ( self.value <= self.user.balance ):
                self.user.balance = self.user.balance - self.value
                destino.balance = destino.balance + self.value 
                try:
                    session.commit()
                    print(' ---------> Operação realizada com sucesso.')
                except:
                    self.user.balance = self.user.balance + self.value
                    destino.balance -= self.value
                    print('Depósito não realizado. Erro: Instabilidade no servidor.')
                

            else:
                print('--------> Saldo insuficiente.')
        else:
            print(" -------> Operação cancelada. Erro: informações de destino erradas.")
                