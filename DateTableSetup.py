import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import psycopg2
from configparser import ConfigParser

Base = declarative_base()
class DateTimeTable():

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
            engine = create_engine(enginestart)
            return engine
        except(Exception) as error:
            print(error)

class DateTable(Base):
    __tablename__ = 'dateTable'
    id =Column(Integer, primary_key = True)
    theDate = Column(DateTime, nullable = False)
    DayOfWeek = Column(String(128), nullable = False)
    DayOfMonth = Column(Integer, nullable = False)


if __name__ == '__main__':    
    db = DateTimeTable()
    engine = db.connect()
    Base.metadata.create_all(engine)