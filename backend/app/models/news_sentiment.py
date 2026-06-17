from sqlalchemy import Column, Integer, Text, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from database.base import Base

class NewsSentiment(Base):
    __tablename__ = "news_sentiment"
    
    id = Column(Integer, primary_key=True)
    label = Column(Text, nullable=False)
    news_feed_id = Column(Integer, ForeignKey("news_feed.id"), nullable=False)
    sentiment = Column(Numeric, nullable=False)
    
    news_feed = relationship(
        "NewsFeed",
        back_populates="news_sentiment"
    )
    
    