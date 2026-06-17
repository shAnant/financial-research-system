import feedparser

feed = feedparser.parse(
    "https://news.google.com/rss/search?q=RELIANCE"
)
print(feed)