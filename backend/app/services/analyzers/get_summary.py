from services.analyzers.financial_context import generate_financial_context
import requests


def get_stock_summary(stock_name):
    response = requests.get(f"http://127.0.0.1:8000/fundamentals/{stock_name}")
    
    data = response.json()["metrics"]
    summary = {}
    summary.update({stock_name : generate_financial_context(data)})
    return summary
