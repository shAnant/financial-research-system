from sqlalchemy import Column, Integer, Date, Numeric, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from database.base import Base

class StockMetric(Base):
    __tablename__ = "stock_metric"
    
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.id"), nullable=False)
    metric_id=  Column(Integer, ForeignKey("metrics.id"), nullable=False)
    fiscal_year = Column(Date)
    value = Column(Numeric)
    __table_args__ = (
        UniqueConstraint(
            "stock_id",
            "metric_id",
            "fiscal_year",
            name="uq_stock_metric"
        ),
    )

    stock = relationship(
        "Stock",
        back_populates="financial_metrics"
    )

    metric = relationship(
        "Metrics",
        back_populates="stock_metrics"
    )
    