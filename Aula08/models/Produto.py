from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import DataError, PendingRollbackError
from models.Geral import  Base, Session, engine

class Produto(Base):
    __tablename__ = "produto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String(20), nullable= False)
    descricao = Column(String(100), nullable=False)
    preco = Column(Float, nullable=False)