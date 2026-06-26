from fastapi import APIRouter # collection of api endpoints
from database.db import SessionLocal
from models.stock_data import StockData
from models.stock import Stock
from models.stocks_indicators import StocksIndicators
from models.metrics import Metrics
from models.statement_type_table import StatementTypeTable
from models.stock_metric import StockMetric
from models.news_feed import NewsFeed
from models.news_sentiment import NewsSentiment
from services.analyzers.profitability import profitability_metrics
from services.analyzers.balance_sheet_strength import balance_sheet_metrics
from services.analyzers.cash_flow import cash_flow_metrics
from services.analyzers.share_holder import share_holder_metrics
from collections import defaultdict
from services.analyzers.fundamental_analyzer import derives_metrics

router = APIRouter() # object router

@router.get("/stocks/{stock_name}/get_id")
def get_stock_id(stock_name):
    db = SessionLocal()
    try:
        stock = db.query(Stock).filter(Stock.symbol == stock_name).first()
        return stock.id if stock else None
    finally:
        db.close()
 
@router.get("/stocks/{stock_name}/get_data")
def get_stocks(stock_name):
    stock_id = get_stock_id(stock_name)
    db = SessionLocal()
    
    try:
        stocks = db.query(StockData).filter(StockData.stock_id == stock_id).all()
        
        return [
            {
                "id" : stock.id,
                "date" : stock.date,
                "_high_" : stock._high_,
                "_low_" : stock._low_,
                "_open_" : stock._open_,
                "_close_" : stock._close_,
                "volume" : stock.volume,
                "adj_close" : stock.adj_close,
            }
            for stock in stocks
        ]
    
    finally :
        db.close()

@router.get("/stocks/stockslist")
def  get_stocks_list():
    db = SessionLocal()
    
    try:
        stocks_list = (
                    db.query(Stock)
                    .order_by(Stock.symbol.asc())
                    .all()
                )
        
        return [
            {
                "id" : stock.id,
                "symbol" : stock.symbol
            }
            for stock in stocks_list
        ]
    finally:
        db.close()
        
@router.get("/stocks/{stock_name}/{start_date}/{end_date}")
def get_stock_history(stock_name, start_date, end_date):
    stock_id = get_stock_id(stock_name)
    db = SessionLocal()
    data = (
        db.query(StockData, StocksIndicators)
        .outerjoin(
            StocksIndicators,
            (StockData.stock_id == StocksIndicators.stock_id)
            & (StockData.id == StocksIndicators.data_id)
        )
        .filter(
            StockData.stock_id == stock_id,
            StockData.date >= start_date,
            StockData.date <= end_date
        )
        .order_by(StockData.date)
        .all()
    )
    return [
    {
        **{
            c.name: getattr(stock, c.name)
            for c in StockData.__table__.columns
        },
        **(
            {
                c.name: getattr(indicator, c.name)
                for c in StocksIndicators.__table__.columns
            }
            if indicator
            else {}
        )
    }
    for stock, indicator in data
]
    
@router.get("/stocks/{stock_name}/metrics")
def get_metrics(stock_name):
    stock_id = get_stock_id(stock_name)
    db = SessionLocal()
    try:
        data = db.query(Stock, StockMetric, Metrics, StatementTypeTable).join(
            StockMetric, (StockMetric.stock_id == Stock.id)
            ).join(
                Metrics, (Metrics.id == StockMetric.metric_id)
            ).join(
                StatementTypeTable, (StatementTypeTable.id == Metrics.statement_id)
            ).filter(
                Stock.id == stock_id
            ).order_by(StockMetric.fiscal_year).all()
    finally:
        db.close()
        
    return [
            {
                "stock": stock.symbol,
                "metric": metric.metric_name,
                "statement_type": statement.statement_type,
                "fiscal_year": stock_metric.fiscal_year,
                "value": float(stock_metric.value)
                if stock_metric.value is not None
                else None
            }
            for stock, stock_metric, metric, statement in data
        ]

@router.get("/stocks/{stock_name}/news")
def get_news(stock_name):
    stock_id = get_stock_id(stock_name)
    db = SessionLocal()
    try:
        data = db.query(NewsFeed, Stock).join(
            Stock, (Stock.id == NewsFeed.stock_id)
        ).filter(
            NewsFeed.stock_id ==stock_id
        ).order_by(
            NewsFeed.date
        ).all()
    finally:
        db.close()
     
    return[
        {
            "id": news.id,
            "stock": stock.symbol,
            "content_id": news.content_id,
            "title": news.title,
            "summary": news.summary,
            "date": news.date,
            "url": news.url,
            "source": news.source
        }
        for news, stock in data
    ]
    
@router.get("/stocks/news/{news_feed_id}")
def get_sentiment(news_feed_id):
    db = SessionLocal()
    try:
        data = db.query(NewsSentiment).filter(NewsSentiment.news_feed_id == news_feed_id).all()
    except Exception as e:
        print(e)
        return False
    finally:
        db.close()
    
    return [
        {
            "news_feed_id" : info.news_feed_id,
            "label" : info.label,
            "sentiment" : info.sentiment
        }
        for info in data
    ]
    
    
@router.get("/stocks/{stock_name}/profitability")
def get_stock_profitability(stock_name):
    db = SessionLocal()
    stock_id = get_stock_id(stock_name)
    try:
        data = db.query(StockMetric, Metrics, StatementTypeTable, Stock).join(
                Metrics, (StockMetric.metric_id == Metrics.id)
            ).join(
                StatementTypeTable, (Metrics.statement_id == StatementTypeTable.id)
            ).join(
                Stock,
                (Stock.id == StockMetric.stock_id)
            ).filter(
                Metrics.metric_name.in_(profitability_metrics),
                Stock.id == stock_id
            ).all()
    except Exception as e:
        return {"error" : e}
    finally:
        db.close()
    grouped = defaultdict(dict)
    for stock_metric, metric, statement_type_table, stock in data:
        grouped[metric.metric_name][stock_metric.fiscal_year] = stock_metric.value
    
    return [
        {
            "stock_id" :  stock.id,
            "stock_name" : stock.symbol,
            "metrics" : grouped
        }
    ]

@router.get("/stocks/{stock_name}/balanceSheetStrength")
def get_balance_sheet_strength(stock_name):
    db = SessionLocal()
    stock_id = get_stock_id(stock_name)
    try:
        data = db.query(StockMetric, Metrics, StatementTypeTable, Stock).join(
                Metrics, (StockMetric.metric_id == Metrics.id)
            ).join(
                StatementTypeTable, (Metrics.statement_id == StatementTypeTable.id)
            ).join(
                Stock,
                (Stock.id == StockMetric.stock_id)
            ).filter(
                Metrics.metric_name.in_(balance_sheet_metrics),
                Stock.id == stock_id
            ).all()
    except Exception as e:
        return {"error" : e}
    finally:
        db.close()
    
    grouped = defaultdict(dict)
    for stock_metric, metric, statement_type_table, stock in data:
        grouped[metric.metric_name][stock_metric.fiscal_year] = stock_metric.value
    
    return [
        {
            "stock_id" :  stock.id,
            "stock_name" : stock.symbol,
            "metrics" : grouped
        }
    ]
    
@router.get("/stocks/{stock_name}/cashFlowMetrics")
def get_cash_flow_metrics(stock_name):
    db = SessionLocal()
    stock_id = get_stock_id(stock_name)
    try:
        data = db.query(StockMetric, Metrics, StatementTypeTable, Stock).join(
                Metrics, (StockMetric.metric_id == Metrics.id)
            ).join(
                StatementTypeTable, (Metrics.statement_id == StatementTypeTable.id)
            ).join(
                Stock,
                (Stock.id == StockMetric.stock_id)
            ).filter(
                Metrics.metric_name.in_(cash_flow_metrics),
                Stock.id == stock_id
            ).all()
    except Exception as e:
        return {"error" : e}
    finally:
        db.close()
    
    grouped = defaultdict(dict)
    for stock_metric, metric, statement_type_table, stock in data:
        grouped[metric.metric_name][stock_metric.fiscal_year] = stock_metric.value
    
    return [
        {
            "stock_id" :  stock.id,
            "stock_name" : stock.symbol,
            "metrics" : grouped
        }
    ]
    
@router.get("/stocks/{stock_name}/shareHolderMetrics")
def get_share_holder_metrics(stock_name):
    db = SessionLocal()
    stock_id = get_stock_id(stock_name)
    try:
        data = db.query(StockMetric, Metrics, StatementTypeTable, Stock).join(
                Metrics, (StockMetric.metric_id == Metrics.id)
            ).join(
                StatementTypeTable, (Metrics.statement_id == StatementTypeTable.id)
            ).join(
                Stock,
                (Stock.id == StockMetric.stock_id)
            ).filter(
                Metrics.metric_name.in_(share_holder_metrics),
                Stock.id == stock_id
            ).all()
    except Exception as e:
        return {"error" : e}
    finally:
        db.close()
    
    grouped = defaultdict(dict)
    for stock_metric, metric, statement_type_table, stock in data:
        grouped[metric.metric_name][stock_metric.fiscal_year] = stock_metric.value
    
    return [
        {
            "stock_id" :  stock.id,
            "stock_name" : stock.symbol,
            "metrics" : grouped
        }
    ]
    

@router.get("/stocks/{stock_name}/{metric_name}")
def get_metric(stock_name, metric_name):
    db = SessionLocal()
    stock_id = get_stock_id(stock_name)
    try:
        data = db.query(StockMetric, Metrics, StatementTypeTable, Stock).join(
                Metrics, (StockMetric.metric_id == Metrics.id)
            ).join(
                StatementTypeTable, (Metrics.statement_id == StatementTypeTable.id)
            ).join(
                Stock,
                (Stock.id == StockMetric.stock_id)
            ).filter(
                Metrics.metric_name == metric_name,
                Stock.id == stock_id
            ).all()
    except Exception as e:
        return {"error" : e}
    finally:
        db.close()
        
    if not data:
        return {
            "error": f"Metric '{metric_name}' not found for {stock_name}"
        }
    
    grouped = defaultdict(dict)
    for stock_metric, metric, statement_type_table, stock in data:
        grouped[metric.metric_name][stock_metric.fiscal_year] = stock_metric.value
    
    if not grouped:
        return {
            "error" : "there is some issue in grouped variable"
        }
    
    return [
        {
            "stock_id" :  stock_id,
            "stock_name" : stock_name,
            "metrics" : grouped
        }
    ]
    
@router.get("/fundamentals/{stock_name}")
def get_fundamentals(stock_name):
    result = derives_metrics(stock_name)
    return result