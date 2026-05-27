from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import DataError, PendingRollbackError
from models.Geral import  Base, Session, engine

class Usuario(Base):
    __tablename__ ='usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(20), nullable = False)
    senha = Column(String(10), nullable = False)
    nome = Column(String(50), nullable = False)