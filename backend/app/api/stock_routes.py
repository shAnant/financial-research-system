from fastapi import APIRouter # collection of api endpoints
from database.db import SessionLocal
from models.stock_data import StockData
from models.stock import Stock
from models.stocks_indicators import StocksIndicators
from models.metrics import Metrics
from models.statement_type_table import StatementTypeTable
from models.stock_metric import StockMetric

router = APIRouter() # object router

@router.get("/stocks/{stock_name}/get_id")
def get_stock_id(stock_name):
    db = SessionLocal()
    try:
        stock = db.query(Stock).filter(Stock.symbol == stock_name).first()
        
        if not stock:
            return {"error":"Stock not found"}
        
        return stock.id
    
    finally:
        db.close()
 
@router.get("/stocks/{stock_name}")
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
        stocks_list = db.query(Stock).all()
        
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
    
@router.get("/{stock_name}/metrics")
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
                "metric": metric.metric_name,  # adjust field name
                "statement_type": statement.statement_type,  # adjust field name
                "fiscal_year": stock_metric.fiscal_year,
                "value": float(stock_metric.value)
                if stock_metric.value is not None
                else None
            }
            for stock, stock_metric, metric, statement in data
        ]
