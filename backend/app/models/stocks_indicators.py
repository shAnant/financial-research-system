from sqlalchemy import Column, Integer, Text, Numeric, ForeignKey
from database.base import Base
from sqlalchemy.orm import relationship

class StocksIndicators(Base):
    __tablename__ = "stocks_indicators"
    id = Column(Integer, primary_key=True, autoincrement=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"))

    return_ = Column("return_", Numeric(10, 2))
    percentage_change = Column(Numeric(10, 2))

    candle_body_size = Column(Numeric(10, 2))
    upper_shadow = Column(Numeric(10, 2))
    lower_shadow = Column(Numeric(10, 2))
    total_range = Column(Numeric(10, 2))
    body_percentage = Column(Numeric(10, 2))
    intraday_volatility = Column(Numeric(10, 2))

    diff_high_prevclose = Column(Numeric(10, 2))
    diff_low_prevclose = Column(Numeric(10, 2))
    true_range = Column(Numeric(10, 2))

    volume_change = Column(Numeric(10, 2))

    sma5 = Column(Numeric(10, 2))
    sma10 = Column(Numeric(10, 2))

    rsi = Column(Numeric(10, 2))

    ema12 = Column(Numeric(10, 2))
    ema26 = Column(Numeric(10, 2))

    macd = Column(Numeric(10, 2))
    atr14 = Column(Numeric(10, 2))

    relative_volume = Column(Numeric(10, 2))

    standard_deviation_20 = Column(Numeric(10, 2))

    middle_band = Column(Numeric(10, 2))
    upper_band = Column(Numeric(10, 2))
    lower_band = Column(Numeric(10, 2))

    return_lag1 = Column(Numeric(10, 2))
    return_lag2 = Column(Numeric(10, 2))
    return_lag3 = Column(Numeric(10, 2))
    return_lag5 = Column(Numeric(10, 2))

    ema_distance_12 = Column(Numeric(10, 2))
    ema_distance_26 = Column(Numeric(10, 2))
    ema_distance_20 = Column(Numeric(10, 2))

    bollinger_width = Column(Numeric(10, 2))
    percent_b = Column(Numeric(10, 2))

    target = Column(Numeric(10, 0))
    data_id = Column(Integer, ForeignKey("stock_data.id"))
    
    stock = relationship(
        "Stock",
        back_populates="indicators"
    )