from sqlalchemy import Column, Integer, Text
from database.base import Base

class Stock(Base):
    __tablename__ = "stocks"
    
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)