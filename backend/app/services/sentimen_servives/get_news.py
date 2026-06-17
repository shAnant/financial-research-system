import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[2])
)
from api.stock_routes import get_news


def fetch_news(stock_name):
    news = []
    try:
        data = get_news(stock_name)
    except Exception as e:
        return {"error":"Stock not found. Please enter a correct stock name"}
    for info in data:
        news.append({
            "id" : info["id"],
            "content_id" : info["content_id"],
            "title" : info["title"],
            "summary" : info["summary"]
        })
    return news