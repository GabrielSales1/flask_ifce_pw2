from models.Geral import Base, String, Integer,Column

class Cliente(Base):
    __tablename__ = 'cliente'
    id = Column(Integer,primary_key=True,autoincrement=True,nullable=False)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    endereco = Column(String(100), nullable=False)
    telefone = Column(String(14), nullable=False)

