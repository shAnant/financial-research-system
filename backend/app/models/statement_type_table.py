from sqlalchemy import Column, Integer, Text
from database.base import Base
from sqlalchemy.orm import relationship

class StatementTypeTable(Base):
    __tablename__ = "statement_type_table"
    
    id = Column(Integer, primary_key=True)
    statement_type = Column(Text)
    
    metrics = relationship(
        "Metrics",
        back_populates="statement_type"
    )