from transformers import pipeline
from get_news import fetch_news
from api.stock_routes import get_sentiment, get_stocks_list
from sentiment_data_push import add_to_news_sentiment_table

classifier = pipeline(
    "sentiment-analysis",
    model = "ProsusAI/finbert",
    framework="pt"
)

def predict_news_sentiment(stock_name):
    news = fetch_news(stock_name)
    output = []
    for info in news:
        news_feed_id = info['id']
        table_data = get_sentiment(news_feed_id)
        if table_data:
            output.append(table_data)
            continue
        else:
            result = classifier(info['summary'])[0]
        instance = {
            "news_feed_id" : news_feed_id,
            "label" : result['label'],
            "sentiment" : result['score']
        }
        output.append(instance)
        add_to_news_sentiment_table(instance)
    return output

stocks = get_stocks_list()
for stock in stocks:
    predict_news_sentiment(stock['symbol'])
    