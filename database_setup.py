import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import psycopg2
from configparser import ConfigParser

Base = declarative_base()
class MonthlyBills():
    
    def __init__(self):
        self.filename ='/home/trock/Desktop/database.ini'
        self.section = 'postgresql'
        
        
    def config(self):
        parser = ConfigParser()
        parser.read(self.filename)
        db = {}
        if parser.has_section(self.section):
            params = parser.items(self.section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section,filename) )
        return db
    def connect(self):
        conn = None
        try:
            params = self.config()
            print(params)
            conn = psycopg2.connect(**params)
            enginestart = 'postgresql+psycopg2://' + params['user'] + ':' + params['password'] + '@' + params['host']  + ':5432/' + params['database']
            print(enginestart)
            engine = create_engine(enginestart)
            return engine
        except(Exception) as error:
            print('there is an error')
            print(error)

class MonthlyBill(Base):
    __tablename__ = 'monthlyBills'
    id = Column(Integer, primary_key = True)
    bill = Column(String(80), nullable = False)
    cost = Column(Float)
    date = Column(String(2))
    UserID = Column(String(128))
    
class WeeklyBill(Base):
    __tablename__ = 'weeklyBills'
    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    dayOfWeek = Column(String(250))
    cost = Column(Float)
    UserID = Column(String(128), nullable = False)

class BringHome(Base):
    __tablename__ = 'bringHomePay'
    id =Column(Integer, primary_key = True)
    name = Column(String(50), nullable = False)
    amount = Column(Float) 
    dayOfWeek =  Column(String(9))
    Frequency = Column(String(25))
    UserID = Column(String(128), nullable = False)

class BankBalance(Base):
    __tablename__ = 'bankBalance'
    id =Column(Integer, primary_key = True)
    balance = Column(Float, nullable = False)
    date = Column(DateTime)
    UserID = Column(String(128), nullable = False)

if __name__ == '__main__':    
    mb = MonthlyBills()
    engine = mb.connect()
#     engine = create_engine('sqlite:///TRBills.db')
    Base.metadata.create_all(engine)
# engine = create_engine('sqlite:///TRBills.db')
    Base.metadata.create_all(engine)