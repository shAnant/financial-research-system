from sqlalchemy import Column, Integer, Text, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base

class NewsFeed(Base):
    __tablename__ = "news_feed"
    
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    content_id = Column(Text, unique=True, nullable=False)
    title = Column(Text, nullable=False)
    summary = Column(Text)
    date = Column(TIMESTAMP)
    url = Column(Text, nullable=False)
    source = Column(Text, nullable=False)
    
    
    stock = relationship(
        "Stock",
        back_populates="news_feed"
    )
    news_sentiment = relationship(
        "NewsSentiment",
        back_populates="news_feed"
    )
    