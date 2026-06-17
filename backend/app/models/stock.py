from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import relationship
from database.base import Base

class Stock(Base):
    __tablename__ = "stocks"
    
    id = Column(Integer, primary_key=True)
    symbol = Column(Text)
    
    indicators = relationship(
        "StocksIndicators",
        back_populates="stock"
    )
    
    financial_metrics = relationship(
    "StockMetric",
    back_populates="stock"
    )
    
    news_feed = relationship(
        "NewsFeed",
        back_populates="stock"
    )