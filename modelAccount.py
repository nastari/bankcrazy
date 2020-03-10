import psycopg2
from datetime import datetime
from sqlalchemy import ( create_engine, Column, MetaData, Table,Integer, String , DateTime, Sequence )
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql+psycopg2://postgres:Desgraca20@localhost/crazybank') 
                            # user:password@host/dbname # LGTM!
metadata = MetaData( bind = engine )
Base = declarative_base( metadata = metadata )
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

class AccountClients(Base):

    __tablename__ = 'clients'
    id = Column( Integer , Sequence('user_id_seq'), primary_key = True )
    name = Column(String(40),nullable = False)
    userLogin = Column(String(40),nullable = False)
    passwordLogin = Column( String(40),nullable = False)
    balance =  Column( Integer, nullable = False , default = 0 )
    create_in = Column( DateTime , default = datetime.now)
    update_in = Column( DateTime , default = datetime.now, onupdate = datetime.now )
    


Base.metadata.create_all(engine)
