import yfinance 

ticker = yfinance.Ticker("RELIANCE.NS")
print(ticker.news)