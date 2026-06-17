from database.db import SessionLocal
from models.news_sentiment import NewsSentiment

def add_to_news_sentiment_table(data):
    db = SessionLocal()
    instance = NewsSentiment(
        label = data['label'],
        news_feed_id = data['news_feed_id'],
        sentiment = data['sentiment']
    )
    try:
        db.add(instance)
        db.commit()
        db.refresh(instance)
        print(f"{data['news_feed_id']} is added to sentiment table")
    
    except Exception as e:
        print(f"Process failed with error : {e}")
        
    finally:
        db.close()