from sqlalchemy import Column, Integer, Text, Float

from database.base import Base

class StockData(Base):
    __tablename__ = "stocks_data"
    
    id = Column(Integer, primary_key=True)
    
    date = Column(Text)
    
    _high_ = Column(Float)
    _low_ = Column(Float)
    _open_ = Column(Float)
    _close_ = Column(Float)
    volume = Column(Float)
    adj_close = Column(Float)
    
    stock_id = Column(Text)