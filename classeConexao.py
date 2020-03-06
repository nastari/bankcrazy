import psycopg2


class Conexao():
    

    def __init__(self):
        self.con = psycopg2.connect(
            host='localhost', 
            database='crazybank', 
            user='postgres', 
            password=''
            )
        self.cur = self.con.cursor()


    def registrarCliente(self,id, nome,cpf,email,contato):

        sql = """ INSERT INTO public.clientes (id, nome ,cpf,email,contato,saldo) VALUES (%s,%s,%s,%s,%s,%s)"""
        dados = (id,nome,cpf,email,contato,0)
        self.cur.execute(sql, dados)
        self.con.commit()
        self.con.close()