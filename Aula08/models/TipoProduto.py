from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import DataError, PendingRollbackError
from models.Geral import  Base, Session, engine

class TipoProduto(Base):
    __tablename__ = "tipoproduto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(100), nullable=False)
    