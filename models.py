from sqlalchemy import Column, Integer, String
from database import Base


class Person(Base):
    __tablename__ = 'people'
    # id = Column(Integer, primary_key=True)
    name = Column(String(256), primary_key=True)
    age = Column(Integer)