from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'usersDup'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    phone = Column(String(15))
