from sqlalchemy import Column, Text, Integer, ForeignKey
from database.base import Base
from sqlalchemy.orm import relationship

class Metrics(Base):
    __tablename__ = "metrics"
    
    id = Column(Integer, primary_key=True)
    metric_name = Column(Text)
    statement_id = Column(Integer, ForeignKey("statement_type_table.id"))
    
    statement_type = relationship(
        "StatementType",
        back_populates="metrics"
    )

    stock_metrics = relationship(
        "StockMetric",
        back_populates="metric"
    )