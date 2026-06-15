from fastapi import APIRouter # collection of api endpoints
from database.db import SessionLocal
from models.stock_data import StockData
from models.stock import Stock
from models.stocks_indicators import StocksIndicators

router = APIRouter() # object router
 
@router.get("/stocks/{stock_id}")
def get_stocks(stock_id):
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

@router.get("/stockslist")
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
        
@router.get("/stocks/{stock_id}/{start_date}/{end_date}")
def get_stock_history(stock_id, start_date, end_date):
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